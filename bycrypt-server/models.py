from sqlalchemy.ext.hybrid import hybrid_property
from app import bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    articles = db.relationship('Article', backref='user')

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))


# bcrypt.generate_password_hash()
# users.password_hash column stores 2 values:
    # the salt
    # the actual return value of Bcrypt

# We run the password we were given in get_json() through Bcrypt along with the salt we read from the database.
