#!/bin/bash

FLASK_APP=app.py
FLASK_ENV=development

export FLASK_APP
export FLASK_ENV

env | grep FLASK_

