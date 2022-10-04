from flask import Flask, jsonify

# Create the main Flask app object
app = Flask(__name__)

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
 
# Run the Flask server and wait for requests
if __name__ == '__main__':
    #app.run()
    app.run(host='127.0.0.1', port='4000')
