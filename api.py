from flask import Flask, request, jsonify

app = Flask(__name__)

# Example endpoint to greet the user
@app.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)