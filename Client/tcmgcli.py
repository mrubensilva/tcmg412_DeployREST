import argparse
import requests

cmd_list = {
  'md5': 'Return the MD5 hash of the string <input>',
  'factorial': 'Return the factorial of the integer <input>',
  'fibonacci': 'Return an array of Fibonacci numbers <= the integer <input>',
  'is-prime': 'Return a boolean that decides if the integer <input> is prime',
  'slack-alert': 'Post <input> to Slack',
  'redis': 'Send <args> to Redis database'
}

parser = argparse.ArgumentParser(description='Access each endpoint in the REST API belonging to TCMG 412 Group 3.', usage='''tcmgcli.py COMMAND <args> <input>\n
commands:
  md5          Return the MD5 hash of string <input>
  factorial    Return the factorial of integer <input>
  fibonacci    Return an array of Fibonacci numbers <= integer <input>
  is-prime     Return a boolean that decides if integer <input> is prime
  slack-alert  Post <input> to Slack
  redis        Send <args> to Redis database
''')
parser.add_argument('COMMAND', nargs='?', default=None, help = 'Subcommand to run (see above)')
parser.add_argument('input', nargs='?', default=None, help = 'String or integer input')
parser.add_argument('-k', '--key', nargs='?', default=None, dest='KEY', help='Use supplied value as key in redis command')
parser.add_argument('-v', '--value', nargs='?', default=None, dest='VALUE', help='Use supplied value as value in redis command')
parser.add_argument('-m', '--method', nargs='?', default=None, dest='METHOD', help='Use supplied value as HTTP method in redis command\nAccepted values are "put", "post", "get", "delete"')

args = parser.parse_args()

if args.COMMAND not in cmd_list:
  print("Unrecognized command")
  parser.print_help()
  exit(1)

if args.COMMAND == 'md5':
  url = 'http://35.208.233.80/md5/' + args.input
  x = requests.get(url)
  jsonResponse = x.json()
  output = jsonResponse['output']
  print(output)

if args.COMMAND == 'factorial':
  try:
    int_arg = int(args.input)
    url = 'http://35.208.233.80/factorial/' + str(int_arg)
    x = requests.get(url)
    jsonResponse = x.json()
    output = jsonResponse['output']
    print(float(output))
  except:
      print('Must use an integer for <input>')

if args.COMMAND == 'fibonacci':
  try:
    int_arg = int(args.input)
    url = 'http://35.208.233.80/fibonacci/' + str(int_arg)
    x = requests.get(url)
    jsonResponse = x.json()
    output = jsonResponse['output']
    print(output)
  except:
      print('Must use an integer for <input>')

if args.COMMAND == 'is-prime':
  try:
    int_arg = int(args.input)
    url = 'http://35.208.233.80/is-prime/' + str(int_arg)
    x = requests.get(url)
    jsonResponse = x.json()
    output = jsonResponse['output']
    print(output)
  except:
      print('Must use an integer for <input>')

if args.COMMAND == 'slack-alert':
  url = 'http://35.208.233.80/slack-alert/' + args.input
  x = requests.get(url)
  jsonResponse = x.json()
  output = jsonResponse['output']
  print(output)

if args.COMMAND == 'redis':
  url = 'http://35.208.233.80/keyval'
  m = args.METHOD
  if m == 'put' or m == 'post':
    if args.KEY:
	    KEY = args.KEY
    else:
	    KEY = input('key: ')
      
    if args.VALUE:
	    VALUE = args.KEY
    else:
	    VALUE = input('value: ')
    r = requests.request(m, url, json={"key": str(KEY), "value": str(VALUE)})
    print(r.json())
  elif m == "get" or m == "delete":
    if args.KEY:
	    KEY = args.KEY
    else:
	    KEY = input('key: ')
  
    r = requests.request(m, url + "/" + str(KEY))
    print(r.json())
  else:
    parser.print_help()
    exit(1)
