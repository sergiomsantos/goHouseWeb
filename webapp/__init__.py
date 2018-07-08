from flask import Flask
# import config


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Flask APP Instantiation
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
app = Flask(__name__)
# app.config.from_object(config.Config)

from webapp import routes
