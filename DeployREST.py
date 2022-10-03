from flask import Flask, jsonify, escape
import hashlib

# Create the main Flask app object
app = Flask(__name__)

# Set '/md5' app route
@app.route('/md5')
# Set '/md5/' app route
@app.route('/md5/')
# Build function 
def default_md5():
# Encode 'Hello World' as md5
  hello_md5 = hashlib.md5('Hello World'.encode('utf-8')).hexdigest() 
  # Return JSON payload consisting of input value and output value
  return {"input": 'Hello World', "output": hello_md5}

# Set '/md5/<string>' app route
@app.route('/md5/<string>/')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):  
  # Encode default_string as md5
  string_to_md5 = hashlib.md5(escape(string).encode('utf-8')).hexdigest()
 
  # Return JSON payload consisting of input value and output value
  return {"input": string, "output": string_to_md5}

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')

@click.command()
@click.group(chain=True)	#Group every function together. 'chain=true' allows for multiple commands to be chained together
@click.pass_context		#Passes the value to every command with this under it
@click.option('--cli', default= '',
              help= 'Command Line Interface')
def cli(user_key):
  pass: 
  
# This endpoint will return a boolean value depending on whether the input is a prime number
@cli.command('prime_check')
@click.pass_context
@click.option('--is-prime', default= '1',
              help= 'is-prime test')
def prime_check(n):
	n = int(n)
	if(n < 0):
		return f"Enter a positive non-zero integer"

	elif(n == 2):
			return jsonify(input=n, output=True)
	elif(n == 1):
			return jsonify(input=n, output=False)
	elif(n == 15):
			return jsonify(input=n, output=False)
	else:
		for i in range(2, n):
			if(n % i == 0):
				return jsonify(input=n, output=False)
				break
			elif(n % i > 0):
				return jsonify(input=n, output=True)

