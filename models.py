from mongoengine import connect, StringField, IntField, Document, DateTimeField
from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps


connect(db="activity_log_db", host="localhost")


class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=str(datetime.utcnow))
    details = StringField(required=True)

    @classmethod
    def get_all_activities(cls):
        activity_log=[]
        for activity in MongoClient().activity_log_db.activity_log.find():
            activity_log.append(activity)
        return dumps(activity_log)

    @classmethod
    def post_log_event(cls, user_id, username, details):
        activity_log=[]
        event = ActivityLog(
            user_id=user_id,
            username=username,
            details=details,
            timestamp=datetime.utcnow()
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