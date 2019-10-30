from flask import url_for, json
from datetime import datetime
import requests
import json
import pytest
from app import app


def test_get_activities():
	get_url = "http://0.0.0.0:5001/api/activities/"
	r = requests.get(get_url)
	data = r.json()
	assert r.status_code == 200
	assert len(data) == 10


def test_get_specific_activities():
	get_url = "http://0.0.0.0:5001/api/activities/1/"
	r = requests.get(get_url)
	data = r.json()
	assert r.status_code == 200
	assert len(data) != 0


def test_post_activity():
	post_url = "http://0.0.0.0:5001/api/activities/"
	new_activity = {
		"user_id": 4,
		"username": "test",
		"timestamp": str(datetime.utcnow()),
		"details": "this is a test"
	}
	r = requests.post(post_url, json=new_activity)
	assert r.status_code == 200