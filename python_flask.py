from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def method_name():
    return "<h1> Hello !!! </h1>"

@app.route('/one')
def method_name1():
    return "<h1> Hello  1   !!! </h1>"

@app.route('/two')
def method_name2():
    return "<h1> Hello  2  !!! </h1>"

@app.route('/sum')
def test():
    a=5+6
    return f"sum {a}"

@app.route('/input_url')
def request_input():
    data= request.args.get('x')
    return f"this is my input from url <h1> {data} </h1>"


if __name__ == '__main__':
    app.run(host = "0.0.0.0")