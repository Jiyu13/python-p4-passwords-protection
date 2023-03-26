from flask.ext.bcrypt import Bcrypt

# instantiate Bcrypt with app instance
bcrypt = Bcrypt(app)

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