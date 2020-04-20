"""
Rasa Conversational AI Application Package Initializer
"""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# # Read settings from config module (blissApp/config.py)
# app.config.from_object('insta485.config')

# if a database is needed,
# from rasaApp.model import get_db


import rasaApp.bls  # noqa: E402  pylint: disable=wrong-import-position
# add additional function imports here