from flask import Flask, request, jsonify
from instagrapi import Client
import os

app = Flask(__name__)

# Initialize Instagrapi client
client = Client()

# Example endpoint to send a direct message
@app.route('/send_message', methods=['GET'])
def send_direct_message():
    try:
        # Get target username and message from the query parameters
        target_username = request.args.get('username')
        message = request.args.get('message')

        # Login to your Instagram account
        client.login('cashflowsensitive', '#CashFlowSensitive08')

        # Get the user ID of the target user
        user_info_dict = client.search_users(target_username)
        target_user_id = user_info_dict[0].pk

        # Send the direct message
        client.direct_send(message, [target_user_id])
        
        return jsonify({"status": "success", "message": "Direct message sent successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/upload', methods=['GET','POST'])
def upload_post():
    # Get data from the POST request
    username = request.args.get('username')
    password = request.args.get('password')
    video_path = request.args.get('video_path')
    caption = request.args.get('caption')

    # Initialize the client
    cl = Client()

    # Log in
    cl.login(username, password)

    # Upload the post
    cl.clip_upload(
        path=video_path,
        caption=caption
    )

    return 'Post uploaded successfully!'

if __name__ == '__main__':
    # Use PORT environment variable if available, or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
