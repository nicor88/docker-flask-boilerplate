import json
import logging

from flask import Flask, Response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('flask-app')

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
