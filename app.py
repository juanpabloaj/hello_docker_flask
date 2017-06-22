from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

process_name = './echo.py'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return jsonify({'message': 'hello world'})


if __name__ == '__main__':
    app.run()
