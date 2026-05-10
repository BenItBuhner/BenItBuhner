param(
    [string]$NodeUrl = "https://explorer.rustchain.org",
    [int]$TimeoutSec = 10
)

$ErrorActionPreference = "Stop"

function Invoke-RustChainJson {
    param([string]$Path)
    $uri = $NodeUrl.TrimEnd("/") + $Path
    try {
        Invoke-RestMethod -Uri $uri -TimeoutSec $TimeoutSec -Headers @{ "User-Agent" = "rustchain-miner-status-powershell/1.0" }
    } catch {
        [PSCustomObject]@{ error = $_.Exception.Message; uri = $uri }
    }
}

$health = Invoke-RustChainJson "/health"
$epoch = Invoke-RustChainJson "/epoch"
$minersResponse = Invoke-RustChainJson "/api/miners"

Write-Host "RustChain Miner Status"
Write-Host "======================"
Write-Host ("Node: {0}" -f $NodeUrl)

if ($health.error) {
    Write-Host ("Health: ERROR - {0}" -f $health.error)
} else {
    Write-Host ("Health: ok={0}, version={1}, db_rw={2}, tip_age_slots={3}" -f $health.ok, $health.version, $health.db_rw, $health.tip_age_slots)
}

if ($epoch.error) {
    Write-Host ("Epoch: ERROR - {0}" -f $epoch.error)
} else {
    Write-Host ("Epoch: {0}, slot={1}, pot={2} RTC, enrolled={3}" -f $epoch.epoch, $epoch.slot, $epoch.epoch_pot, $epoch.enrolled_miners)
}

if ($minersResponse.error) {
    Write-Host ("Miners: ERROR - {0}" -f $minersResponse.error)
    exit 1
}

$miners = @($minersResponse.miners)
Write-Host ("Active miner records: {0}" -f $miners.Count)
$miners |
    Sort-Object -Property last_attest -Descending |
    Select-Object -First 20 |
    Format-Table miner, device_family, device_arch, antiquity_multiplier, last_attest -AutoSize

if ($health.error -or $epoch.error) {
    exit 1
}
