#hey there..
from flask import Flask, jsonify, request
from datetime import datetime
from models import ActivityLog


app = Flask(__name__)


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


user1 = (1,'jordan')
user2 = (2, 'jordan2')


details = 'this is a test'


@app.route('/api/activities/', methods=['GET'])
def get_activity():
    return ActivityLog.get_all_activities()


@app.route('/api/activities/<specific_id>/', methods=['GET'])
def get_specific_user_activity(specific_id):
    return ActivityLog.get_specific_user_event(int(specific_id))


@app.route('/api/activities/', methods=['POST'])
def post_activity():
    return ActivityLog.post_log_event(request.json['user_id'], request.json['username'], request.json['details'])


if __name__ == '__main__':
    app.run(debug=True)