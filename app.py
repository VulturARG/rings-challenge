from flask import Flask, jsonify

from domain.gateway.exceptions import GatewayException
from domain.star_wars.exceptions import StarWarsException
from domain.utils.wiring import ManageStarWarsWiring

app = Flask(__name__)

API_STAR_WARS_URL = "https://swapi.dev/api/"


@app.route('/api/v1/<name>', methods=['GET'])
def get(name: str):
    try:
        wiring = ManageStarWarsWiring.for_production(API_STAR_WARS_URL)
        star_wars_service = wiring.get_manage_message()
        return jsonify(star_wars_service.get_message(name))
    except (GatewayException, StarWarsException) as error:
        return jsonify(
            {
                "status": "error",
                "description": error.MESSAGE,
            }
        )


if __name__ == '__main__':
    app.run()
