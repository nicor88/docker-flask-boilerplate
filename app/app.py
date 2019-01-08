import json
import logging

from flask import Flask, Response

import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('flask-app')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_route():
    try:
        payload = {'output': 'Hello World from Flask'}
        return Response(
            response=json.dumps(payload),
            status=200,
            mimetype='application/json'
        )
    except Exception as error:
        logger.error(error)
        return Response(
            response=json.dumps({'error': 'Application error'}),
            status=500,
            mimetype='application/json'
        )


@app.route('/all_users', methods=['GET', 'POST'])
def all_users():
    try:
        users_count = db.get_users_count()
        payload = {'output': f'The total number of users is {users_count}'}
        return Response(
            response=json.dumps(payload),
            status=200,
            mimetype='application/json'
        )
    except Exception as error:
        logger.error(error)
        return Response(
            response=json.dumps({'error': 'Application error'}),
            status=500,
            mimetype='application/json'
        )


@app.route('/users', methods=['GET', 'POST'])
def users():
    try:
        payload = {'users': list(db.get_users())}
        return Response(
            response=json.dumps(payload),
            status=200,
            mimetype='application/json'
        )
    except Exception as error:
        logger.error(error)
        return Response(
            response=json.dumps({'error': 'Application error'}),
            status=500,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
