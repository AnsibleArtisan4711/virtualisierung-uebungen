<#
.SYNOPSIS
    Inventarisiert alle VMs des Hosts als Tabelle und CSV-Datei (Modul 07, Aufgabe 3).
.DESCRIPTION
    Je VM: Name, Status, Konfigurationsversion, vCPUs, zugewiesener RAM, Größe der Festplattendateien,
    Anzahl und Alter der Checkpoints. Nur lesend; geschrieben wird allein die CSV-Datei.
    Entwurf: nicht ausgeführt.
.PARAMETER CsvPath
    Zieldatei (Standard: C:\HyperV\VM_Inventory.csv).
.PARAMETER MaxCheckpointAgeDays
    Checkpoints, die älter sind, werden als Warnung ausgegeben (Standard: 7).
.EXAMPLE
    .\Get-HyperVReport.ps1 -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$CsvPath = 'C:\HyperV\VM_Inventory.csv',
    [int]$MaxCheckpointAgeDays = 7
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$rows = foreach ($vm in Get-VM) {
    $checkpoints = @(Get-VMCheckpoint -VMName $vm.Name)
    $oldestDays = $null
    if ($checkpoints.Count -gt 0) {
        $oldest = ($checkpoints | Sort-Object -Property CreationTime | Select-Object -First 1).CreationTime
        $oldestDays = [math]::Round(((Get-Date) - $oldest).TotalDays, 1)
    }
    $diskBytes = 0
    foreach ($d in Get-VMHardDiskDrive -VMName $vm.Name) {
        if ($d.Path -and (Test-Path -Path $d.Path)) {
            $diskBytes += (Get-Item -Path $d.Path).Length
        }
    }
    [pscustomobject]@{
        Name                 = $vm.Name
        State                = $vm.State
        Version              = $vm.Version
        vCPU                 = $vm.ProcessorCount
        MemoryAssignedMB     = [math]::Round($vm.MemoryAssigned / 1MB)
        DiskFilesGB          = [math]::Round($diskBytes / 1GB, 2)
        Checkpoints          = $checkpoints.Count
        OldestCheckpointDays = $oldestDays
    }
}

$rows | Sort-Object -Property Name | Format-Table -AutoSize

foreach ($r in $rows) {
    if ($null -ne $r.OldestCheckpointDays -and $r.OldestCheckpointDays -gt $MaxCheckpointAgeDays) {
        Write-Warning ("{0}: ältester Checkpoint {1} Tage alt (Grenze {2})" -f $r.Name, $r.OldestCheckpointDays, $MaxCheckpointAgeDays)
    }
}

if ($PSCmdlet.ShouldProcess($CsvPath, 'CSV-Datei schreiben')) {
    $rows | Sort-Object -Property Name | Export-Csv -Path $CsvPath -NoTypeInformation -Encoding UTF8
    Write-Host "CSV geschrieben: $CsvPath"
}
