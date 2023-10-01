#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print('Received parameter:', parameter)
    return f'<h1> Printed string {parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a list of numbers in the range of the parameter
    numbers = range(1,parameter + 1)

    # Create an HTML string with each number on a separate line
    numbers_html = "<br>".join(map(str, numbers))

    # Display the numbers in the web browser
    return f'<h1>Counting Numbers:</h1><p>{numbers_html}</p>'

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math (num1, operation, num2):
    result = None   #setting value for result as None. None is a special object that represents the absence of a value or a null value.

    # Perform the appropriate operation based on the provided operation parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, %"

    # Display the result in the web browser
    return f'<h1>Result: {result}</h1>'









if __name__ == '__main__':
    app.run(port=5555, debug=True)
