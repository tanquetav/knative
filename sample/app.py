from flask import Flask, request
import json
app = Flask(__name__)

def info():
    return "version 1.0"

@app.route('/')
def hello_world():
    return json.dumps({"info":info()}), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
