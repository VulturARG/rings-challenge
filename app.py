from flask import Flask, jsonify

from domain.gateway.exceptions import GatewayException
from domain.star_wars.exceptions import StarWarsException
from domain.utils.get_mesage import get_message

app = Flask(__name__)

API_STAR_WARS_URL = "https://swapi.dev/api/"


@app.route('/api/v1/<name>', methods=['GET'])
def get(name: str):
    try:
        return jsonify(get_message(name, API_STAR_WARS_URL))
    except (GatewayException, StarWarsException) as error:
        return jsonify(
            {
                "status": "error",
                "description": error.MESSAGE,
            }
        )


if __name__ == '__main__':
    app.run()
