from flask import Flask, jsonify, escape

def fib(n):     # assumes that n > 0
    f_1, f_2 = 0, 1
    ret = [0]
    while f_2 <= n:
        ret.append(f_2)
        f_1, f_2 = f_2, f_1 + f_2
    return ret

# Create the main Flask app object
app = Flask(__name__)

@app.route('/fibonacci/<int:number>')
def fibonacci(number=1):
        if int(number) < 0:
            return "Error: not a valid number"
        return jsonify(input = number, output = fib(number))

# Run the Flask server and wait for requests
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000')
