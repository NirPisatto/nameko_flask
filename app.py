from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.json.get('name')
    message = f'Hello, {name}!'
    return jsonify({'message': message})


@app.route('/hello', methods=['GET'])
def hello():
    message = "Hello War"
    return message



if __name__ == '__main__':
    app.run(debug=True)


