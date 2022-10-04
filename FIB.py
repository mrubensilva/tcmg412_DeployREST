from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/<int:number>')
def fibonacci(number=1):
    return jsonify(input = "fib(" + str(number) + "): ", output = str(fib(number)))
    #return "Howdy!!<hr>fib("+ str(number) + "): " + str(fib(number))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    if n < 0:
        return "Error: not a valid number"

# Return JSON payload consisting of input value and output value
    return {"input": number, "output": fibonacci }

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
