from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Example endpoint to greet the user
@app.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    # Use PORT environment variable if available, or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
