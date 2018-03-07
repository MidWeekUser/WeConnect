# run.py

from app import app_factory

app = app_factory('DevelopmentConfig')

if __name__ == '__main__':
    app.run()