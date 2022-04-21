from flask import Flask, jsonify

from domain.gateway.exceptions import GatewayException
from domain.utils.get_mesage import get_message

app = Flask(__name__)

API_STAR_WARS_URL = "https://swapi.dev/api/"


@app.route('/api/v1/<name>', methods=['GET'])
def get(name: str):
    """Get characters by name."""

    try:
        response = get_message(name, API_STAR_WARS_URL)
        return jsonify(response)
    except GatewayException as error:
        return jsonify(
            {
                "status": "error",
                "description": error.MESSAGE,
            }
        )


if __name__ == '__main__':
    app.run()
