from flask import Flask, request, jsonify
import uuid
import requests

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        # Get the message from the POST request
        message = request.get_data(as_text=True)
        # Generate a unique ID for the message
        unique_id = str(uuid.uuid4())
        # Create the payload to send to external services
        payload = {'id': unique_id, 'message': message}
        
        try:
            # Send the payload to the logging service
            log_response = requests.post('http://localhost:5001/log', json=payload)
            log_response.raise_for_status()
            
            # Send the payload to the messages service
            message_response = requests.post('http://localhost:5002/message', json=payload)
            message_response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            # Return an error response if any request fails
            return jsonify({"status": "error", "message": str(e)}), 500

        # Return a success response with the unique ID
        return jsonify({"status": "message received", "id": unique_id}), 201
    
    elif request.method == 'GET':
        try:
            # Get logs from the logging service
            log_response = requests.get('http://localhost:5001/logs')
            log_response.raise_for_status()
            
            # Get messages from the messages service
            message_response = requests.get('http://localhost:5002/messages')
            message_response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            # Return an error response if any request fails
            return jsonify({"status": "error", "message": str(e)}), 500

        # Return the logs and messages in the response
        return jsonify({
            "logs": log_response.json(),
            "messages": message_response.json()
        })

if __name__ == '__main__':
    # Start the Flask application
    with app.app_context():
        app.run(port=5000, debug=True)
