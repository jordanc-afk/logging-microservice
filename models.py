from mongoengine import connect, StringField, IntField, Document, DateTimeField
from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps


connect(db="activity_log_db", host="localhost")


class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

    @classmethod
    def get_all_activities(cls):
        activity_list=[]
        for activity in MongoClient().activity_log_db.activity_log.find():
            activity_list.append(activity)
        return dumps(activity_list)

    @classmethod
    def post_log_event(cls, user, details):
        activity_list=[]
        event = ActivityLog(
            user_id=user.user_id,
            username=user.username,
            details=details,
            timestamp=datetime.utcnow()
            )
        event.save()
        for activity in MongoClient().activity_log_db.activity_log.find({'timestamp': event.timestamp}):
            activity_list.append(activity)
        return dumps(activity_list)

    @classmethod
    def get_specific_user_event(cls, specific_user):
        activity_list=[]
        for activity in MongoClient().activity_log_db.activity_log.find({'user_id': specific_user}):
            activity_list.append(activity)
        return dumps(activity_list)