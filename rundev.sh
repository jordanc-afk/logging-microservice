#!/bin/bash
export FLASK_DEBUG=1
export ACTIVITIES_GET=10
export DB=activity_log_db
export DB_CONNECTION='mongodb+srv://activity-logger-dbUser:g%3FfmgBMrGCRVivNysXD9hsqJ@cluster0-khbtl.mongodb.net/activity_log_database?retryWrites=true&w=majority'
export DB_PORT=27017
flask run --host=0.0.0.0 --port=5001 --debugger
