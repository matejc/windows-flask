# Flask on Windows containers (example)

This is a Native Windows solution

I am normally a ferocious Linux-only user, but production requires stability and that comes in form of simplicity!
No Docker Desktop or Docker Linux-containers on Windows or WSL, since those are development environments (I do not care if someone says that any of those solutions are production ready - they are not and never will be)


## Pre-requirements: Setup Docker for Windows containers

Run PowerShell as Administrator and run:

```
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1
.\install-docker-ce.ps1
```

Source: https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce


## Build docker image

Clone this repository, change directory to inside it and run (in PowerShell obviously):

```
docker build . -t flask
```


## Running

```
docker run -ti --rm -p 8000:8000 flask
```

To check, go to http://127.0.0.1:8000 in your browser.


## What next?

Nginx? Not in this case! If you have money for Windows VPS/machine then go for load-balancer. Even smaller VPS providers have that.
