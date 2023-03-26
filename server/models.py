from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    # protected attr from inadvertent modification
    _password_hash = db.Column(db.String, nullable=False)

    articles = db.relationship('Article', backref='user')

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'


    # this is a special property decorator for sqlalchemy
    # it leaves all of the sqlalchemy characteristics of the column in place
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    # hybrid_property allows us to manipulate any column,
    # and the manipulated value can be accessed like any other db query
    
    
    # setter method for the password property
    @password.setter
    def password_hash(self, password):
        self._password_hash = self.simple_hash(password)

    # authentication method using user and password
    def authenticate(self, password):
        return self.simple_hash(password) == self.password_hash  # password_hash is the function in line 20
        # return True/False

    # simple_hash requires no access to the class or instance
    # let's leave it static
    @staticmethod
    def simple_hash(input):
        return sum(bytearray(input, encoding="utf-8"))