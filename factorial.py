from flask import Flask
import hashlib

# Create the main Flask app object
app = Flask(__name__)

# Set '/factorial' app route
@app.route('/factorial')
# Set '/factorial/' app route
@app.route('/factorial/')
# Build function 
def factorial():
# get the input
    factorialInput = int(input("What number do you want the factorial of?: "))
    factorialOutput = 1
#calculate the factorial
    for i in range(1, factorialInput + 1):
        factorialOutput = factorialOutput * i
# Return JSON payload consisting of input value and output value
    return {"input": factorialInput, "output": factorialOutput}

# Set '/factorial/<num>' app route
@app.route('/factorial/<num>/')
# Pass value of '<num>' to 'num' in 'factorial_made' function
def factorial_made(num):  
    factorialOutput = 1
#calculate the factorial
    num1 = int(num)
    for i in range(1, num1 + 1):
        factorialOutput = factorialOutput * i
 
  # Return JSON payload consisting of input value and output value
    return {"input": num, "output": factorialOutput}

# Run the Flask server and wait for requests
if __name__ == '__main__':
    #app.run()
    app.run(host='127.0.0.1', port='4000')
