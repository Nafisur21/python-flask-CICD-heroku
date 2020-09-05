from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "Hello, Nafisur!"


@app.route("/test", methods=['POST'])
def webhook():
    data = request.get_json()
    name = data['name']
    title = data['title']
    message = f'As-Salam-Alaikum {name} {title}'
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
