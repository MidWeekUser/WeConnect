# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user_registration')
def user_registration():
    return render_template("user_registration.html")

@app.route('/user_login')
def user_login():
    return render_template("user_login.html")

@app.route('/business_registration')
def business_registration():
    return render_template("business_registration.html")

@app.route('/business_profile')
def business_profile():
    return render_template("business_profile.html")

@app.route('/business_update')
def business_update():
    return render_template("business_update.html")

@app.route('/business_catalog')
def business_catalog():
    return render_template("business_catalog.html")
