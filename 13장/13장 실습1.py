from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/hello/")
def hello2():
    return "<h1>안녕, 순천향!!</h1>"


if __name__ == "__main__":
    app.run()
