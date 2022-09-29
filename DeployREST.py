from flask import Flask
import hashlib

# Create the main Flask app object
app = Flask(__name__)

# Use the magic decorator to map a function to a URL
@app.route('/')
def hello_world():
  
  # In the most basic case, just returning a string from the function will tell Flask
  #   to send back the string as the HTTP response body with default headers
  return "<h1>Hello, World!</h1>"


# Here's an example of including a variable in the URL, and passing it into the function
@app.route('/howdy/<name>')
def howdy_world():
  
  # Setting up a default value, in case none is provided in the URL
  addressee = 'World'
  
  # Check to see if 'name' has a value, and overwrite the default
  if name:
    addressee = name
  
  # Use a Python f-string to customize the return value
  return f"<h1>Howdy, {addressee}!</h1>"

# Set '/md5/<string>' app route
@app.route('/md5/<string>')
# Pass value of '<string>' to 'string' in 'md5_encode' function
def md5_encode(string):

  # Set default value for 'default_string' if no value in '<string>'
  default_string = 'Hello World'
  
  # Overwrite 'default_string' if 'string' has value
  if string:
    default_string = str(string)

  # Encode default_string as md5
 
  string_to_md5 = hashlib.md5(default_string.encode('utf-8')).hexdigest()
 
  # Print 'string' and 'string_to_md5' to site

  return f"<h1>String</h1>\n{default_string}\n<h2>MD5</h2>\n{string_to_md5}"

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
