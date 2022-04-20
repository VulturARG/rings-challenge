from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/')
def hello_world():  # put application's code here
    return f'Get {id}'


if __name__ == '__main__':
    app.run()
