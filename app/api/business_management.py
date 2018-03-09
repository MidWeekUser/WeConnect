from flask import Flask, jsonify, request
from flask_restplus import Resource, Api, fields
try:
    from app.models import BusinessManagement
except Exception:
    from WeConnect.app.models import BusinessManagement

business_data = []
business_review_data = []

BusinessObj = BusinessManagement()

class RegisterBusinesses(Resource):
    def post(self):

        business_data = request.json
        businessname = business_data['businessname']
        category = business_data['category']
        location = business_data['location']

        status = BusinessObj.registernewbusiness(businessname, category, location)
        
        return status
    
    def get(self):
        response = []
        for business in BusinessObj.business_data:
            response.append(business.todict())
        return response

class AddBusinessReview(Resource):
    def post(self):

        business_review_data = request.json
        new_business_review = business_review_data['businessreview']
        status = BusinessObj.post_new_business_review(new_business_review)
        
        return status
    
    def get(self):
        response = []
        for business in BusinessObj.business_review_data:
            response.append(business.todict())
        return response