<#
.SYNOPSIS
    Stellt hostseitig die Ausgangslage nach Modul 08 wieder her (Modul 12, Aufgabe 1).
.DESCRIPTION
    Für VM-SRV01 und VM-SRV02: ausschalten (falls nötig), Virtualisierungserweiterungen aus,
    MAC-Adressen-Spoofing aus, statischer Arbeitsspeicher 2048 MB. Bereits erreichte Zustände werden übersprungen.
    Die Schritte INNERHALB der Gast-VMs (VM-NESTED01 löschen, Switch Nested-Privat entfernen, Hyper-V-Rolle
    deinstallieren) macht dieses Skript nicht.
    Unterstützt -WhatIf. Entwurf: nicht ausgeführt.
.PARAMETER VMName
    Betroffene VMs (Standard: VM-SRV01, VM-SRV02).
.EXAMPLE
    .\Reset-NestedLab.ps1 -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [string[]]$VMName = @('VM-SRV01', 'VM-SRV02'),
    [uint64]$StartupBytes = 2048MB
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

foreach ($n in $VMName) {
    $vm = Get-VM -Name $n -ErrorAction SilentlyContinue
    if (-not $vm) { Write-Warning "VM $n nicht gefunden - übersprungen."; continue }

    $proc = Get-VMProcessor -VMName $n
    $mem  = Get-VMMemory -VMName $n
    $nics = @(Get-VMNetworkAdapter -VMName $n)
    $needsChange = $proc.ExposeVirtualizationExtensions -or $mem.DynamicMemoryEnabled -or
                   ($mem.Startup -ne $StartupBytes) -or
                   (@($nics | Where-Object { $_.MacAddressSpoofing -eq 'On' }).Count -gt 0)

    if (-not $needsChange) { Write-Host "$n : bereits in der Ausgangslage."; continue }

    if ($PSCmdlet.ShouldProcess($n, 'Ausgangslage herstellen (VM wird ausgeschaltet)')) {
        if ($vm.State -ne 'Off') { Stop-VM -Name $n -Force }
        Set-VMProcessor -VMName $n -ExposeVirtualizationExtensions $false
        Set-VMNetworkAdapter -VMName $n -MacAddressSpoofing Off
        Set-VMMemory -VMName $n -DynamicMemoryEnabled $false -StartupBytes $StartupBytes
        Write-Host "$n : zurückgesetzt (ausgeschaltet)."
    }
}
Write-Host 'Danach VMs starten und mit Get-LabState.ps1 prüfen.'
