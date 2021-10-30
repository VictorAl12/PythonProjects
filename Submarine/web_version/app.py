from flask import Flask, render_template, request
import json
from submarine import Submarine


app = Flask(__name__)


@app.route('/', methods=['GET'])
def render():
    return render_template('index.html')

@app.route('/order-sub', methods=['POST'])
def order():
    data = request.data
    data = json.loads(data)

    direction = data['direction'].upper()
    if direction == 'NORTH':
        direction = 0
    elif direction == 'EAST':
        direction = 1
    elif direction == 'SOUTH':
        direction = 2
    elif direction == 'WEST':
        direction = 3

    sub = Submarine(int(data['x']), int(data['y']), int(data['z']), direction)
    result = sub.command(data['orders'])

    return {'result': result}