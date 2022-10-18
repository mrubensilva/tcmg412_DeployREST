import string
import requests
from urllib import request, response
from flask import Flask, jsonify, escape
import hashlib
from slackeventsapi import SlackEventAdapter

def fib(n):     # assumes that n > 0
    f_1, f_2 = 0, 1
    ret = [0]
    while f_2 <= n:
        ret.append(f_2)
        f_1, f_2 = f_2, f_1 + f_2
    return ret

# Create the main Flask app object
app = Flask(__name__)

# Set '/md5/<string>' app route
@app.route('/md5/<string>')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):  
  # Encode default_string as md5
  string_to_md5 = hashlib.md5(escape(string).encode('utf-8')).hexdigest()
 
  # Return JSON payload consisting of input value and output value
  return jsonify(input = string, output = string_to_md5)
  
# Set '/factorial/<num>' app route
@app.route('/factorial/<int:num>')
# Pass value of '<num>' to 'num' in 'factorial_made' function
def factorial_made(num):
    factorialOutput = 1
    if num < 0:
        return jsonify(input = num, output = "That's not a valid number!")

    #calculate the factorial
    for i in range(1, num + 1):
        factorialOutput = factorialOutput * i
    # Return JSON payload consisting of input value and output value
    return jsonify(input = num, output = factorialOutput)
    
@app.route('/fibonacci/<int:number>')
def fibonacci(number=1):
        if int(number) < 0:
            return "Error: not a valid number"
        return jsonify(input = number, output = fib(number))
            

#slack alert
@app.route('/slack-alert/<text>')
def slack_alert(text):
    url = "https://hooks.slack.com/services/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"  
    slack_data = {'text': 'message'}

    # use the `requests` module to POST to Slack
    r = requests.post(url, json=slack_data)

    # you can check the status code of the response from Slack
    if r.status_code == 200:
       return jsonify(input = text, output = "it works")

    else:
        return "it doesnt work", 404


# Set '/is-prime/<int>' app route
@app.route('/is-prime/<n>')
def is_prime(n): 
  try:
    n = int(n) 

    if n == 1:
        return jsonify(input=n, output=False)

    solve_prime = int(n / 2)
    for i in range(2, solve_prime):
        if n % i == 0:
            return jsonify(input=n, output=False)

    return jsonify(input=n, output=True)

  except:
    return "Error not a number", 404
   
  

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
