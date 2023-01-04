# CLI Client for RESTful API

## Server Status: DOWN
This client was programmed to send requests to `http://35.208.233.80/`, a remote instance of the RESTful API server running in Google Cloud. However, this remote instance is now offline for the sake of my budget :P

## Usage
`docker pull msilv204/tcmg412_cli`  
`docker run msilv204/tcmg412_cli <input> <args>`

### Examples
`docker run msilv204/tcmg412_cli md5 test`  
`docker run msilv204/tcmg412_cli redis -k foo -v bar -m post`
