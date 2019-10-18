#hey there..
from flask import Flask, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': 'important stuff here',
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': 'important stuff here',
    },
]


@app.route('/api/activity_log/', methods=['GET'])
def get_activity():
    return jsonify({'activity_log': activity_log})


@app.route('/api/activity_log/<int:activity_id>/', methods=['GET'])
def get_specific_activity(activity_id):
    # activity = [lambda x: x['id'] == activity_id, activity_log]
    for item in filter(lambda x: x['id'] == activity_id, activity_log):
        return jsonify({'activity_log': item})


@app.route('/api/activity_log/', methods=['POST'])
def post_activity():
    new_activity = {
        'id': activity_log[-1]['id'] + 1,
        'user_id': activity_log[-1]['user_id'] + 1,
        'username': request.json['username'],
        'timestamp': datetime.utcnow(),
        'details': request.json['details']
    }
    activity_log.append(new_activity)
    return jsonify({'activity_log': new_activity})


if __name__ == '__main__':
    app.run(debug=True)