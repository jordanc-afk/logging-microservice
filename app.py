#hey there..
from flask import Flask
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