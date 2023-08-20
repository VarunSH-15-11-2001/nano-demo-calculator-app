from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    n = request.get_json()['first']
    m = request.get_json()['second']
    k = n+m
    return str(n+m), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    n = request.get_json()['first']
    m = request.get_json()['second']
    k = n-m
    return str(n-m), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
