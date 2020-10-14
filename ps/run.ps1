. "$pwd\ps\functions"

switch($args[0]) {
    start {
        Invoke-DockerSetup
    }
    stop {
        Remove-BackendSetup
    }
    default {}
}
