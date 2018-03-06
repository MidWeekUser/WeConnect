from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
# @api.route('/hello')

class RegisterUsers(Resource):
    def get(self):
        return {'hello':'world'}

api.add_resource(RegisterUsers, '/registeruser')

if __name__ == '__main__':
    app.run(debug=True)