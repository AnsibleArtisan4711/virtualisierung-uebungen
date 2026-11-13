<#
.SYNOPSIS
    Legt die Test-VM VM-AUTO01 (Generation 2) an oder entfernt sie wieder (Modul 07, Aufgabe 2).
.DESCRIPTION
    Anlegen: dynamische VHDX, Generation-2-VM, SCSI-Anbindung, Switch, Startaktion Nothing, Stoppaktion ShutDown.
    Entfernen (-Remove): VM und VHDX werden gelöscht.
    Beide Richtungen unterstützen -WhatIf. Entwurf: nicht ausgeführt.
    Die Parameter von New-VM, New-VHD und Add-VMHardDiskDrive sind teilweise gegen Microsoft Learn gelesen,
    -AutomaticStartAction und -AutomaticStopAction von Set-VM nicht.
.PARAMETER Name
    Name der VM (Standard: VM-AUTO01).
.PARAMETER SwitchName
    Virtueller Switch (Standard: vSwitch-Privat-Lab).
.PARAMETER Remove
    Entfernt die VM und ihre VHDX, statt sie anzulegen.
.EXAMPLE
    .\Deploy-TestVM.ps1 -WhatIf
.EXAMPLE
    .\Deploy-TestVM.ps1
.EXAMPLE
    .\Deploy-TestVM.ps1 -Remove
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
param(
    [string]$Name = 'VM-AUTO01',
    [string]$SwitchName = 'vSwitch-Privat-Lab',
    [string]$VmRoot = 'C:\HyperV\VMs',
    [string]$VhdRoot = 'C:\HyperV\VHDs',
    [uint64]$MemoryStartupBytes = 1GB,
    [uint64]$VhdSizeBytes = 20GB,
    [switch]$Remove
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$vhdPath = Join-Path -Path $VhdRoot -ChildPath "$Name.vhdx"
$existing = Get-VM -Name $Name -ErrorAction SilentlyContinue

if ($Remove) {
    if ($existing) {
        if ($PSCmdlet.ShouldProcess($Name, 'VM ausschalten und entfernen')) {
            if ($existing.State -ne 'Off') { Stop-VM -Name $Name -TurnOff -Force }
            Remove-VM -Name $Name -Force
        }
    } else {
        Write-Warning "VM $Name nicht vorhanden."
    }
    if (Test-Path -Path $vhdPath) {
        if ($PSCmdlet.ShouldProcess($vhdPath, 'VHDX löschen')) {
            Remove-Item -Path $vhdPath -Force
        }
    }
    return
}

if ($existing) { throw "Die VM $Name existiert bereits. Zuerst mit -Remove entfernen." }
if (-not (Get-VMSwitch -Name $SwitchName -ErrorAction SilentlyContinue)) {
    throw "Der Switch $SwitchName existiert nicht (Modul 03)."
}
if (Test-Path -Path $vhdPath) { throw "Die Datei $vhdPath existiert bereits." }

if ($PSCmdlet.ShouldProcess($Name, 'VM mit VHDX anlegen')) {
    New-VHD -Path $vhdPath -SizeBytes $VhdSizeBytes -Dynamic | Out-Null
    New-VM -Name $Name -Generation 2 -MemoryStartupBytes $MemoryStartupBytes -NoVHD -Path $VmRoot -SwitchName $SwitchName | Out-Null
    Add-VMHardDiskDrive -VMName $Name -ControllerType SCSI -ControllerNumber 0 -Path $vhdPath
    Set-VM -Name $Name -AutomaticStartAction Nothing -AutomaticStopAction ShutDown
    Get-VM -Name $Name | Format-List Name, Generation, State, MemoryStartup, AutomaticStartAction, AutomaticStopAction
}
