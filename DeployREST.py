from flask import Flask, jsonify, escape
import hashlib

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

# Check if program is called directly (like `python basic_flask.py`),
# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
