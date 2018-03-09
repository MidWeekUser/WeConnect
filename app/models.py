from flask_restplus import fields
import re, uuid


class User:
    def __init__(self, user_id, email, username, firstname, secondname, password, confirmpassword):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.firstname = firstname
        self.secondname = secondname
        self.password = password
        self.confirmpassword = confirmpassword

    def todict(self):
        print(self.user_id)
        return {'username': self.username,  'secondname': self.secondname, 'firstname': self.firstname}

class Business:
    def __init__(self, businessname, category, location):
        self.businessname = businessname
        self.category = category
        self.location = location
    
    def todict(self):
        return {'Business Name': self.businessname, 'Category': self.category, 'Location': self.location}

class Business_Review:
    def __init__(self, business_review):
        self.business_review = business_review
    
    def todict(self):
        return {'Business Review': self.business_review}

class UserManagement:

    def __init__(self):
        self.user_data = []
        self.login_info = []
    
    
    def registernewuser(self, user_id, email, firstname, secondname, username, password, confirmpassword):
        newuser = User(user_id = user_id, email = email, firstname = firstname, secondname = secondname, username = username, password = password, confirmpassword = confirmpassword)
        SpecialSym = ['$','@','#','/','^','(',')','-','%','&','!','*']

        for registeredusers in self.user_data:
            if registeredusers.username == newuser.username:
                return {"Error!": "This username is not available"}
            elif registeredusers.email == newuser.email:
                return {"Error!": "This e-mail is already registered"}
            
        if not firstname.isalpha():
                return {"Error!": "Your first name is incorrect"}

        elif not secondname.isalpha():
                return {"Error!": "Your second name is incorrect"}
        
        elif not username:
                return {"Error!": "A username is required"}
        
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                return {"Error!": "E-Mail address isn't valid"}

        elif not password:
            return {"Error!":"A password is required"}

        elif len(password) <8:
            return {"Error!":"The password should be atleast 8 characters long"}

        elif not any(char.isupper() for char in password):
            return {"Error":"The password should have at least one uppercase letter"}

        elif not any(char.islower() for char in password):
            return {"Error!":"The password should have at least one lowercase letter"}

        elif not any(char in SpecialSym for char in password):
            return {"Error!":"The password should have at least one of the symbols ($@#/*-&^%!)"}

        elif not any(char.isdigit() for char in password):
            return {"Error!":"The password should have at least one numeral"}
        
        elif password != confirmpassword:
            return {"Error!":"Passwords do not match"}

        self.user_data.append(newuser)

        return {"Success!":"You've been registered"}, 201

    def delete_user(self, username):
        try:
            del self.user_data[username]
        except KeyError:
            pass
        return {"Success!":"You've been registered"}


class BusinessManagement:

    def __init__(self):
        self.business_data = []
        self.business_review_data = []
    
    def registernewbusiness(self, businessname, category, location):
        newbusiness = Business(businessname = businessname, category = category, location = location)
        
        for registeredbusinesses in self.business_data:
            if registeredbusinesses.businessname == newbusiness.businessname:
                return {"Error!": "This business already exists"}
        
        if not businessname:
            return {"Error!": "A business name is required"}

        elif not category.isalpha():
            return {"Error!": "The infomation you submitted for category is incorrect"}

        elif not location:
            return {"Error!": "The location of your business is required"}
        
        self.business_data.append(newbusiness)

        return {"Success!":"Your business has been registered"}
    
    
    def post_new_business_review(self, business_review):
        new_business_review = Business_Review(business_review = business_review)
        
        self.business_review_data.append(new_business_review)

        return {"Success!":"Your review has been posted."}        
