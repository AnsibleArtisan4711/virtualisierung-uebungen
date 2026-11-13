<#
.SYNOPSIS
    Zeigt nur lesend den Zustand des Labors: virtuelle Switches, VM-Grunddaten und Netzwerkadapter.
.DESCRIPTION
    Hilfsmittel für die Rückbauschritte der Module 03, 05, 08 und 12. Es wird nichts verändert.
    Entwurf: nicht ausgeführt. Die Eigenschaftsnamen (z. B. PortMirroringMode, VlanSetting) vor dem Einsatz prüfen.
.PARAMETER VMName
    VMs, die angezeigt werden sollen (Standard: VM-SRV01 und VM-SRV02).
.EXAMPLE
    .\Get-LabState.ps1
#>
[CmdletBinding()]
param(
    [string[]]$VMName = @('VM-SRV01', 'VM-SRV02')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host '--- Virtuelle Switches ---'
Get-VMSwitch | Select-Object Name, SwitchType | Format-Table -AutoSize

Write-Host '--- Virtuelle Maschinen ---'
foreach ($n in $VMName) {
    $vm = Get-VM -Name $n -ErrorAction SilentlyContinue
    if (-not $vm) { Write-Warning "VM $n nicht gefunden"; continue }
    $mem  = Get-VMMemory -VMName $n
    $proc = Get-VMProcessor -VMName $n
    [pscustomobject]@{
        Name          = $vm.Name
        State         = $vm.State
        Generation    = $vm.Generation
        vCPU          = $proc.Count
        ExposeVirtExt = $proc.ExposeVirtualizationExtensions
        DynamicMemory = $mem.DynamicMemoryEnabled
        StartupMB     = [math]::Round($mem.Startup / 1MB)
    }
} | Format-Table -AutoSize

Write-Host '--- Netzwerkadapter ---'
Get-VMNetworkAdapter -VMName $VMName |
    Select-Object VMName, Name, SwitchName, Connected, MacAddressSpoofing, DhcpGuard, RouterGuard, PortMirroringMode |
    Format-Table -AutoSize
