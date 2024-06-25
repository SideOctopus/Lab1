from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store logs
log_storage = {}

@app.route('/log', methods=['POST'])
def log_message():
    # Get the JSON data from the POST request
    data = request.get_json()
    # Store the message in log_storage with the unique ID as the key
    log_storage[data['id']] = data['message']
    # Return a success response
    return jsonify({"status": "logged"}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    # Return all stored logs
    return jsonify(log_storage)

if __name__ == '__main__':
    # Start the Flask application for logging service
    app.run(port=5001, debug=True)
