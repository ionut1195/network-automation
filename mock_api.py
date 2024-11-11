from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/servers", methods=["GET"])
def get_servers():
    with open("server_config.json") as f:
        data = f.read()

    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5000)
