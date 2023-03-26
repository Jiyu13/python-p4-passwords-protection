# define a simple hash function
# def simple_hash(input):
#     return sum(bytearray(input, encoding='utf-8'))


class Login(Resource):

    def post(self):

        username = request.get_json()['username']
        user = User.query.filter(User.username==username).first()

        password = request.get_json()['password']

        # calling the instance method authenticate() from models.py
        if user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200
        
        return {'error': 'Invalid username or password'}, 401


# save the ps hashes in the db, not the password themselves
# a user's ps is set by calling user.password = "<new_ps>", programatically or manually by in administrator
# but simple_hash() is simple, and poor choice