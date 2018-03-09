from flask import Flask
from flask_restplus import Resource, Api
from .api.user_management import RegisterUsers
from .api.business_management import RegisterBusinesses, AddBusinessReview
try:
    from WeConnect.config import DevelopmentConfig, TestingConfig
except Exception:
    from config import DevelopmentConfig, TestingConfig

def app_factory(environment):
    app = Flask(__name__)
    api = Api(app)
    
    if environment == 'DevelopmentConfig':
        app.config.from_object(DevelopmentConfig)
        
    elif environment == 'TestingConfig':
        app.config.from_object(TestingConfig)

    api.add_resource(RegisterUsers, '/api/auth/registeruser')
    api.add_resource(RegisterBusinesses, '/api/businesses')
    api.add_resource(AddBusinessReview, '/api/businesses/reviews')

    return app