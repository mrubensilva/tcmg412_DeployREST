import argparse
import requests

parser = argparse.ArgumentParser(description='Access each endpoint in the REST API belonging to TCMG 412 Group 3.', usage='''tcmgcli.py COMMAND <input>\n
commands:
  md5          Return the MD5 hash of the string input
  factorial    Return the factorial of the integer input
  fibonacci    Return an array of Fibonacci numbers <= the integer input
  is-prime     Return a boolean to decide if the integer input is prime
  slack-alert
''')
parser.add_argument('COMMAND', help = 'Subcommand to run (see "commands:")')
parser.add_argument('input', help = 'String or integer argument')
args = parser.parse_args()

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
