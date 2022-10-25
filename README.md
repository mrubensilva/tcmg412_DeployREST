# tcmg412_DeployREST

[https://app-6eu4mzqmma-uc.a.run.app/](https://app-6eu4mzqmma-uc.a.run.app/)

## Build from source
### Prerequisites
Review the following sections in the [Installation Documentation for Flask](https://flask.palletsprojects.com/en/2.2.x/installation/):
- Virtual environments
- Create an environment
- Activate the environment
- Install Flask

`(venv)─[~/Desktop/DeployREST] $ pip install slackeventsapi` 

### Running the app 
`(venv)─[~/Desktop/DeployREST] $ python server.py`

## Run with Docker
`docker pull msilv204/deployrest-tcmg412:latest`  
`docker run -p 8000:4000 msilv204/deployrest-tcmg412:latest`  
[https://hub.docker.com/r/msilv204/deployrest-tcmg412](https://hub.docker.com/r/msilv204/deployrest-tcmg412)
