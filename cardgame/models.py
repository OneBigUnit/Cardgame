from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from cardgame import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    p1_wins = db.Column(db.Integer, nullable=False, default=0)
    p1_losses = db.Column(db.Integer, nullable=False, default=0)
    p1_rounds_won = db.Column(db.Integer, nullable=False, default=0)
    p1_rounds_lost = db.Column(db.Integer, nullable=False, default=0)
    p1_record_points = db.Column(db.Integer, nullable=False, default=0)
    p2_wins = db.Column(db.Integer, nullable=False, default=0)
    p2_losses = db.Column(db.Integer, nullable=False, default=0)
    p2_rounds_won = db.Column(db.Integer, nullable=False, default=0)
    p2_rounds_lost = db.Column(db.Integer, nullable=False, default=0)
    p2_record_points = db.Column(db.Integer, nullable=False, default=0)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
