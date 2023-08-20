from flask import Flask, requests

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    n = requests['first']
    m = requests['second']
    k = n+m
    return '%d'%k, 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    n = requests['first']
    m = requests['second']
    k = n-m
    return '%d'%k, 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
