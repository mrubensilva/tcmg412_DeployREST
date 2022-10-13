# tcmg412_DeployREST

## Build from source
### Prerequisites
Review the following sections in the [Installation Documentation for Flask](https://flask.palletsprojects.com/en/2.2.x/installation/):
- Virtual environments
- Create an environment
- Activate the environment
- Install Flask

`(venv)─[~/Desktop/DeployREST] $ pip install slackeventsapi` 

### Running the app 
`(venv)─[~/Desktop/DeployREST] $ python DeployRestFinal.py`

## Run with Docker
`docker pull msilv204/deployrest-tcmg412:latest`  
`docker run -p 8000:4000 msilv204/deployrest-tcmg412:latest`
