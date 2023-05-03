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

@app.route('/get_prime', methods=['GET'])
def get_prime():
    prime = []
    for i in range(1, 1001):
        if is_prime(i):
           prime.append(i)

    return prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)


