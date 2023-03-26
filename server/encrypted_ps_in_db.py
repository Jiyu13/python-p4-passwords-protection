class Login(Resource):

    def post(self):
        username = request.get_json['username']
        password = request.get_json()['password']

        #=================== insecure to store ps in db unencrypted ================
        # find user in the db by username from the login in form
        user = User.query.filter(User.usrname==username).first()
        # check if the password from the login form matches the password in the db, 
        if password == user.password:
            # if match, set value of session 'user_id" 
            session["user_id"] = user.id
            return user.to_dict(), 200
        
        return {"error": "Invalid username or password"}, 401
        # =========================================================================
