#!/bin/bash
export FLASK_DEBUG=1
export ATLAS_CONNECTION=mongodb+srv://activity-logger-dbUser:g%3FfmgBMrGCRVivNysXD9hsqJ@cluster0-khbtl.mongodb.net/test?retryWrites=true&w=majority
flask run --host=0.0.0.0 --port=5001 --debugger
