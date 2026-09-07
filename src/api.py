from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello_world():
    name = request.args.get("name")
    if name:
        return jsonify({"message": f"Hello, {name}!"})
    return jsonify({"message": "Hello, World!"})