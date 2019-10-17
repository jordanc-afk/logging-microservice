#hey there..
from flask import Flask, jsonify
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
		'timestamp': 'john',
		'details': 'important stuff here',
	},
]

@app.route('/api/activity_log', methods=['GET'])
def get_activites():
	return jsonify({'activity_log': activity_log})

if __name__ == '__main__':
	app.run(debug=True)