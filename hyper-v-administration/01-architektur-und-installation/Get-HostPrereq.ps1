<#
.SYNOPSIS
    Prüft nur lesend, ob der Host die Voraussetzungen für Hyper-V erfüllt (Modul 01, Aufgabe 1).
.DESCRIPTION
    Liest Prozessor, Arbeitsspeicher, Betriebssystem, die Hyper-V-Eigenschaften von Get-ComputerInfo
    und den Status der Dienste vmms und vmcompute. Es wird nichts verändert.
    Entwurf: nicht ausgeführt. Die Namen der Eigenschaften HyperV* mit Get-ComputerInfo | Get-Member prüfen.
.PARAMETER ReportPath
    Optional: Textdatei, in die das Ergebnis zusätzlich geschrieben wird.
.EXAMPLE
    .\Get-HostPrereq.ps1 -ReportPath C:\HyperV\Prereq.txt
#>
[CmdletBinding()]
param(
    [string]$ReportPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$cpus = @(Get-CimInstance -ClassName Win32_Processor)
$cs   = Get-CimInstance -ClassName Win32_ComputerSystem
$os   = Get-CimInstance -ClassName Win32_OperatingSystem

$result = [ordered]@{
    Computer       = $env:COMPUTERNAME
    Betriebssystem = $os.Caption
    Version        = $os.Version
    Prozessor      = $cpus[0].Name
    Kerne          = ($cpus | Measure-Object -Property NumberOfCores -Sum).Sum
    LogischeProz   = ($cpus | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
    RAM_GB         = [math]::Round($cs.TotalPhysicalMemory / 1GB, 1)
}

# Hyper-V-Anforderungen laut Get-ComputerInfo (Eigenschaften beginnen mit HyperV)
$hv = Get-ComputerInfo -Property 'HyperV*'
foreach ($p in $hv.PSObject.Properties) {
    $result[$p.Name] = $p.Value
}

# Dienste der Hyper-V-Rolle (nach der Installation vorhanden)
foreach ($svc in 'vmms', 'vmcompute') {
    $s = Get-Service -Name $svc -ErrorAction SilentlyContinue
    $result["Dienst_$svc"] = if ($s) { $s.Status } else { 'nicht vorhanden' }
}

# Freier Platz auf C:
$c = Get-PSDrive -Name C
$result['C_frei_GB'] = [math]::Round($c.Free / 1GB, 1)

$obj = [pscustomobject]$result
$obj | Format-List
if ($ReportPath) {
    $obj | Format-List | Out-String | Set-Content -Path $ReportPath -Encoding UTF8
    Write-Host "Bericht geschrieben: $ReportPath"
}
