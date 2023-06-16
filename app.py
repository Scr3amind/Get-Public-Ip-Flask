from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200