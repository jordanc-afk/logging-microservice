from mongoengine import connect, StringField, IntField, Document, DateTimeField
from datetime import datetime
from pymongo import MongoClient
import os
import json
from bson.json_util import dumps


connect(db="activity_log_db", host="localhost")


class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

    @classmethod
    def get_activities(cls):
        activities = ActivityLog.objects.all().order_by("-timestamp").limit(10)
        return dumps(activities)

    @classmethod
    def post_log_event(cls, user_id, username, details, timestamp):
        activity_log=[]
        event = ActivityLog(
            user_id=user_id,
            username=username,
            details=details,
            timestamp=timestamp,
            )
        event.save()
        for activity in MongoClient().activity_log_db.activity_log.find({'timestamp': event.timestamp}):
            activity_log.append(activity)
        return dumps(activity_log)

    @classmethod
    def get_specific_user_event(cls, specific_user):
        activity_log=[]
        for activity in MongoClient().activity_log_db.activity_log.find({'user_id': specific_user}):
            activity_log.append(activity)
        return dumps(activity_log)