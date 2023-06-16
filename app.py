from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({'ip': ip}), 200