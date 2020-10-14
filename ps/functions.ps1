
function Invoke-DockerSetup {
    docker-compose up --build
}

function Remove-DockerSetup {
    docker-composer down
}
