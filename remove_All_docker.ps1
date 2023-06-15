docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker system prune
# Delete all Docker images on the system
docker image ls | ForEach-Object { docker image rm -f $_.ID }
Remove-Item C:\ProgramData\Docker\windowsfilter\* -Recurse
