from flask import Flask, request, jsonify
from models import ActivityLog


app = Flask(__name__)


@app.route('/api/activities/', methods=['GET'])
def get_activity():
    return jsonify(ActivityLog.get_activities())


@app.route('/api/activities/<specific_id>/', methods=['GET'])
def get_specific_activity(specific_id):
    return ActivityLog.get_specific_event(int(specific_id))


@app.route('/api/activities/', methods=['POST'])
def post_activity():
    return ActivityLog.post_log_event(request.json['user_id'], request.json['username'], request.json['details'], request.json['timestamp'])


if __name__ == '__main__':
    app.run(debug=True)
