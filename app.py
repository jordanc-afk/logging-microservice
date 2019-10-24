#hey there..
from flask import Flask, jsonify
from datetime import datetime
from models import ActivityLog


app = Flask(__name__)


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


user1 = User(1, "jordan")
user2 = User(2, "jordan2")


nice = "nice"


details = 'this is just a test'


@app.route('/api/ActivityLog/', methods=['GET'])
def get_activity():
    return ActivityLog.get_all_activities()


@app.route('/api/ActivityLog/<int:specific_id>/', methods=['GET'])
def get_specific_user_activity(specific_id):
    return ActivityLog.get_specific_user_event(specific_id)


@app.route('/api/ActivityLog/1/', methods=['POST'])
def post_activity():
    return ActivityLog.post_log_event(user2, details)


if __name__ == '__main__':
    app.run(debug=True)