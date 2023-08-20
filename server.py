from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    n = int(request.get_json()['first'])
    m = int(request.get_json()['second'])
    k = n+m
    res = f"result: {k}"
    return jsonify(res)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    n = request.get_json()['first']
    m = request.get_json()['second']
    k = n-m
    print(k)
    return jsonify(n-m)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
