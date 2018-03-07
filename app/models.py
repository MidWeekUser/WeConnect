from flask_restplus import fields

class User:
    def __init__(self, email, username, firstname, secondname, password, confirmpassword):
        self.username = username
        self.firstname = firstname
        self.secondname = secondname
        self.password = password
        self.confirmpassword = confirmpassword

    def todict(self):
        return {'username': self.username, 'secondname': self.secondname, 'firstname': self.firstname}

class UserManagement:

    def __init__(self):
        self.user_data = []
        self.login_info = []
    
    
    def registernewuser(self, email, firstname, secondname, username, password, confirmpassword):
        newuser = User(email = email, firstname = firstname, secondname = secondname, username = username, password = password, confirmpassword = confirmpassword)
        
        for registeredusers in self.user_data:
            if registeredusers.username == newuser.username:
                return {"Error!": "This username is not available"}
            elif registeredusers.email == newuser.email:
                return {"Error!": "This e-mail is already registered"}
        
        if password != confirmpassword:
            return {"Error!":"Passwords do not match"}

        self.user_data.append(newuser)

        return {"Success!":"You've been registered"}

