from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from application import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)    
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return 'User({}, {}, {})'.format(self.email, self.name, self.surname)


#region Model PersonalInfo - (default) db table
class Personal_Info(db.Model):
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    cell_number = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    cover_letter = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    hobbies = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return 'Personal_Info({}, {}, {}, {}, {}, {})'.format(self.email, self.cell_number, self.address, self.cover_letter, self.position, self.hobbies)
      
#endregion
