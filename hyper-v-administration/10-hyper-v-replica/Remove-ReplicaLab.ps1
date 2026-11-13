<#
.SYNOPSIS
    Baut die Hyper-V-Replica-Testumgebung aus Modul 10 zurück (Aufgabe 3, Rückbau). Läuft lokal in VM-SRV01 bzw. VM-SRV02.
.DESCRIPTION
    Entfernt: Replikation der VM, Replikatserver-Funktion, Firewallregeln (Replikat-Listener, FPS-SMB-In-TCP),
    die selbstsignierten Testzertifikate (Speicher My und Root), .cer-Dateien, Replikatspeicher
    und die beiden hosts-Einträge. Die Replikat-VM wird nur mit -RemoveReplicaVM gelöscht (nur auf VM-SRV02 verwenden!).
    Unterstützt -WhatIf. Entwurf: nicht ausgeführt.
.PARAMETER VMName
    Name der replizierten VM (Standard: VM-NESTED01).
.PARAMETER ReplicaStorage
    Speicherpfad des Replikats (Standard: C:\ReplicaStorage).
.PARAMETER RemoveReplicaVM
    Löscht zusätzlich die Replikat-VM. Nur auf dem Zielserver VM-SRV02 verwenden.
.EXAMPLE
    .\Remove-ReplicaLab.ps1 -WhatIf
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [string]$VMName = 'VM-NESTED01',
    [string]$ReplicaStorage = 'C:\ReplicaStorage',
    [switch]$RemoveReplicaVM
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# 1. Replikation entfernen
if (Get-VMReplication -VMName $VMName -ErrorAction SilentlyContinue) {
    if ($PSCmdlet.ShouldProcess($VMName, 'Replikation entfernen')) {
        Remove-VMReplication -VMName $VMName
    }
}

# 2. Replikat-VM löschen (nur auf Wunsch)
if ($RemoveReplicaVM -and (Get-VM -Name $VMName -ErrorAction SilentlyContinue)) {
    if ($PSCmdlet.ShouldProcess($VMName, 'Replikat-VM löschen')) {
        $vm = Get-VM -Name $VMName
        if ($vm.State -ne 'Off') { Stop-VM -Name $VMName -TurnOff -Force }
        Remove-VM -Name $VMName -Force
    }
}

# 3. Replikatserver-Funktion abschalten
if ($PSCmdlet.ShouldProcess($env:COMPUTERNAME, 'Replikatserver-Funktion abschalten')) {
    Set-VMReplicationServer -ReplicationEnabled $false
}

# 4. Firewallregeln
$rules = @(Get-NetFirewallRule | Where-Object { $_.DisplayName -match 'Replica|Replikat' })
foreach ($r in $rules) {
    if ($PSCmdlet.ShouldProcess($r.DisplayName, 'Firewallregel deaktivieren')) {
        Disable-NetFirewallRule -Name $r.Name
    }
}
if ($PSCmdlet.ShouldProcess('FPS-SMB-In-TCP', 'Firewallregel deaktivieren')) {
    Disable-NetFirewallRule -Name 'FPS-SMB-In-TCP'
}

# 5. Testzertifikate (Speicher My und Root) und .cer-Dateien
foreach ($store in 'My', 'Root') {
    $certs = @(Get-ChildItem -Path "Cert:\LocalMachine\$store" |
        Where-Object { $_.Subject -match '^CN=VM-SRV0[12]$' })
    foreach ($c in $certs) {
        if ($PSCmdlet.ShouldProcess("$store : $($c.Subject)", 'Zertifikat entfernen')) {
            Remove-Item -Path $c.PSPath
        }
    }
}
foreach ($f in @(Get-ChildItem -Path 'C:\' -Filter 'VM-SRV0*.cer' -ErrorAction SilentlyContinue)) {
    if ($PSCmdlet.ShouldProcess($f.FullName, '.cer-Datei löschen')) { Remove-Item -Path $f.FullName -Force }
}

# 6. Replikatspeicher
if (Test-Path -Path $ReplicaStorage) {
    if ($PSCmdlet.ShouldProcess($ReplicaStorage, 'Ordner löschen')) {
        Remove-Item -Path $ReplicaStorage -Recurse -Force
    }
}

# 7. hosts-Einträge
$hosts = Join-Path -Path $env:SystemRoot -ChildPath 'System32\drivers\etc\hosts'
$lines = Get-Content -Path $hosts
$keep  = @($lines | Where-Object { $_ -notmatch '^\s*10\.10\.20\.1[12]\s+VM-SRV0[12]\s*$' })
if ($keep.Count -ne $lines.Count) {
    if ($PSCmdlet.ShouldProcess($hosts, 'Einträge für VM-SRV01 und VM-SRV02 entfernen')) {
        Set-Content -Path $hosts -Value $keep
    }
}
Write-Host 'Rückbau abgeschlossen. Mit Get-VMReplication, Get-NetFirewallRule und Cert:\ prüfen.'
