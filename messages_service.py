from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store messages
messages_storage = {}

@app.route('/message', methods=['POST'])
def save_message():
    # Get the JSON data from the POST request
    data = request.get_json()
    # Store the message in messages_storage with the unique ID as the key
    messages_storage[data['id']] = data['message']
    # Return a success response
    return jsonify({"status": "message saved"}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    # Return all stored messages
    return jsonify(messages_storage)

if __name__ == '__main__':
    # Start the Flask application for messages service
    app.run(port=5002, debug=True)
