import os, string, hashlib, redis, requests
from flask import Flask, jsonify, request, escape
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

# Redis connector
r = redis.Redis(host='redis', port=int(os.environ.get("PORT", 6379)))
		
# Write a new key-value pair into Redis db (CREATE)
@app.route('/keyval', methods=['POST'])
def post_keyval():	
	
	try:
		request_data = request.get_json()
		key = request_data['key']
		value = request_data['value']
		command = f"CREATE {key}/{value}"
	except:
		return jsonify(key = "", value = "", command = "CREATE {key}/{value}", result = "false", error = "Invalid request"), 400
	
				
	if r.exists(key) == 0:
		r.set(key, value)
		return jsonify(key = key, value = value, command = command, result = "true", error = ""), 200
	elif r.exists(key) == 1:
		return jsonify(key = key, value = value, command = command, result = "false", error = "Key already exists"), 409
#Read value given key
@app.route('/keyval', methods=['GET'])
def get_keyval():
	try:
		key = string
		command = f"READ {key}"
		
	except: 
		return jsonify(key = "", value = "", command = "READ {key}/{value}", result = "false", error = "Invalid Request"), 404

	if r.exists(key) == 1:
		value = r.get(key)
		return jsonify(key = key, value = value, command = command, result = "true", error = ""), 200

	elif r.exists(key) == 0: 
		return jsonify(key = key, value = value, command = command, result = "false", error = "key does not exist"), 404

# Overwrite key-value pair in Redis db (UPDATE)
@app.route('/keyval', methods=['PUT'])
def put_keyval():
	
	try:
		request_data = request.get_json()
		key = request_data['key']
		value = request_data['value']
		command = f"UPDATE {key}/{value}"
	except:
		return jsonify(key = "", value = "", command = "UPDATE {key}/{value}", result = "false", error = "Invalid request"), 400	
	
	if r.exists(key) == 0:
		return jsonify(key = key, value = value, command = command, result = "false", error = "Key does not exist"), 404
	elif r.exists(key) == 1:
		r.set(key, value)
		return jsonify(key = key, value = value, command = command, result = "true", error = ""), 200				
			

# Delete Redis db value associated with key in string (DELETE)
@app.route('/keyval/<string>', methods=['DELETE'])
def del_keyval(string):
	try:
		key = string
		command = f"DELETE {key}"
	except:
		return jsonify(key = "", value = "", command = "DELETE {key}", result = "false", error = "Invalid request"), 400
	
	if r.exists(key) == 1: 
		value = f"{r.get(key)}"
		r.delete(key)
		return jsonify(key = key, value = value, command = command, result = "true", error = ""), 200			
	elif r.exists(key) == 0: 
		return jsonify(key = key, value = "", command = command, result = "false", error = "Key does not exist"), 404

		
		
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
    req = requests.post(url, json=slack_data)

    # you can check the status code of the response from Slack
    if req.status_code == 200:
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
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 4000)))
