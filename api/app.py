from flask import Flask, request, jsonify, make_response
from flask_nameko import FlaskPooledClusterRpcProxy

rpc = FlaskPooledClusterRpcProxy()


def create_app():
    app = Flask(__name__)

    app.config.update(
        {
            "NAMEKO_AMQP_URI": "pyamqp://guest:guest@localhost",
            "NAMEKO_INITIAL_CONNECTIONS": 8,
            "NAMEKO_MAX_CONNECTIONS": 16,
            "NAMEKO_RPC_TIMEOUT": 120,
        }
    )

    rpc.init_app(app)

    return app


app = create_app()


@app.route("/greet", methods=["GET"])
def greet():
    message = f"Hello!"
    return jsonify({"message": message})


@app.route("/task_1", methods=["GET"])
def task_1():
    message = rpc.service_rpc.task_1("task 1")

    return message


@app.route("/get_primes", methods=["GET"])
def get_primes():
    primes = []

    primes = rpc.service_rpc.get_primes(100000)

    return make_response(jsonify({"primes": primes}), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
