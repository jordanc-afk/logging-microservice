from mongoengine import connect, IntField, StringField, DateTimeField, Document
from datetime import datetime
import os
import time


sleep_time = os.getenv('SLEEP_TIME', default=0)


db = connect(db=os.environ['DB'], host=os.environ['DB_CONNECTION'], port=int(os.environ['DB_PORT']))


class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

    @classmethod
    def get_activities(cls):
        activities = ActivityLog.objects.all().order_by("-timestamp").limit(10)
        return activities.to_json()

    @classmethod
    def post_log_event(cls, user_id, username, details, timestamp):
        event = ActivityLog(
            user_id=user_id,
            username=username,
            details=details,
            timestamp=timestamp
        )
        event.save()
        time.sleep(int(sleep_time))
        recently_added = ActivityLog.objects(timestamp=event.timestamp).get()
        return recently_added.to_json()

    @classmethod
    def get_specific_event(cls, specific_id):
        specific_activity = ActivityLog.objects(id=specific_id).get()
        return specific_activity.to_json()
