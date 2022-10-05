from flask import Flask, jsonify, escape
import hashlib
import slack
from slackeventsapi import SlackEventAdapter

# Create the main Flask app object
app = Flask(__name__)

# Set '/md5/<string>' app route
@app.route('/md5/<string>/')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):  
  # Encode default_string as md5
  string_to_md5 = hashlib.md5(escape(string).encode('utf-8')).hexdigest()
 
  # Return JSON payload consisting of input value and output value
  return {"input": string, "output": string_to_md5}


  # Set '/factorial' app route
@app.route('/factorial')
# Set '/factorial/' app route
@app.route('/factorial/')
# Build function 
def factorial():
    factorialOutput = 1

    while True:
        try:
            # get the input
            factorialInput = int(input("What number do you want the factorial of?: "))
            #calculate the factorial
            if (factorialInput > 0):
                for i in range(1, factorialInput + 1):
                    factorialOutput = factorialOutput * i
            # Return JSON payload consisting of input value and output value
                return jsonify(input = factorialInput, output = factorialOutput)
            else:
                return jsonify(input = factorialInput, output = "That's not a valid number!")
            break
        except:
            return jsonify(input = factorialInput, output = "That's not a valid number!")

# Set '/factorial/<num>' app route
@app.route('/factorial/<num>/')
# Pass value of '<num>' to 'num' in 'factorial_made' function
def factorial_made(num):
    factorialOutput = 1
    
    while True:
        try:
            num1 = int(num)
            if num1 < 0:
                return jsonify(input = num, output = "That's not a valid number!")
            #calculate the factorial
            
            for i in range(1, num1 + 1):
                factorialOutput = factorialOutput * i
            # Return JSON payload consisting of input value and output value
            return jsonify(input = num, output = factorialOutput)
        except:
            return jsonify(input = num, output = "That's not a valid number!")

@app.route('/fibonacci')

@app.route('/fibonacci/<int:number>')
def fibonacci(number=1):
    while True:
        try:
            n1 = int(number)
            if int(n1) < 0:
                return "Error: not a valid number"
            return jsonify(input = "fib(" + str(number) + "): ", output = str(fib(number)))
        except:
            return jsonify(input = n1, output = "not a valid number")
        
    #return "Howdy!!<hr>fib("+ str(number) + "): " + str(fib(number))

def fib(n):
    while True:
        try:
            n1 = int(n)
            if int(n1) < 0:
                return "Error: not a valid number"
            if n1 == 0:
                return 0
            elif n1 == 1:
                return 1
            else:
                return fib(n1 - 1) + fib(n1 - 2)
        except:
            return jsonify(input = n1, output = "not a valid number")

#slack alert
# SLACK_TOKEN="<xoxb-4176399459060-4173888784227-TEB1KPyN1XJzJB5EL4JasfrV>"
# SIGNING_SECRET="<c1adeb5ae4fea9963fc9939accf460f2>"
 
# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
 
# client = slack.WebClient(token=SLACK_TOKEN)
 
# @ slack_event_adapter.on('message')
# def message(payload):
#     print(payload)
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')
 
#     if text == "Hi":
#         client.chat_postMessage(channel=channel_id,text=">^..^<")

# Set '/is-prime/<int:n>' app route
@app.route('/is-prime/<int:n>')
def test_prime(n):
    if (n==1):
        return {"input": n, "output": False}
    elif (n==2):
        return {"input": n, "output": True}
    else:
        for x in range(2,n):
            if(n % x==0):
                return {"input": n, "output": False}
        return {"input": n, "output": True}    

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
 
