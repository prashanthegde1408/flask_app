from flask import Flask,render_template

app = Flask(__name__)


@app.route('/welcome')
def method_name1():
    return "<h1> Welcome to ABC Corporation </h1>"

@app.route('/')
def method_name2():
    return render_template('index')


if __name__ == '__main__':
    app.run(host = "0.0.0.0")