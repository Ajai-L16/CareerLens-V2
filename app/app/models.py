from app import app, db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# UserMixin provides default implementations for Flask-Login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # This creates a one-to-many relationship
    # A user can have many analyses.
    analyses = db.relationship('Analysis', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_description = db.Column(db.Text, nullable=False)
    ats_score = db.Column(db.Float, nullable=False)
    matching_skills = db.Column(db.Text, nullable=True)  # Storing as JSON string
    missing_skills = db.Column(db.Text, nullable=True)  # Storing as JSON string
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # This is the foreign key that links to the User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Analysis('Score: {self.ats_score}', 'Date: {self.date_posted}')"