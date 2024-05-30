from . import db
from flask_login import UserMixin
from datetime import datetime
from app import login_manager
from hashlib import md5
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    """User model for storing user information."""
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.Text(200))
    profile_picture = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    skills = db.relationship('UserSkills', backref='user', lazy=True)
    projects = db.relationship('UserProject', backref='user', lazy=True)

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
    

    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class UserSkills(db.Model):
    """Association table for user and skill."""
    __tablename__ = 'user_skills'
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        primary_key=True
    )
    skill_id = db.Column(
        db.Integer,
        db.ForeignKey('skills.skill_id'),
        primary_key=True
    )

class Skill(db.Model):
    """Skill model for storing skills."""
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

class Project(db.Model):
    """Model representing a project in the application."""
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_by_user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.user_id'), 
        nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserProject(db.Model):
    """Association table for user and project."""
    __tablename__ = 'user_projects'
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        primary_key=True
    )
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.project_id'),
        primary_key=True
    )
    role = db.Column(
        db.Enum(
            'owner',
            'member',
            'collaborator',
            name='user_project_role'
        ),
        default='member'
    )
    status = db.Column(
        db.Enum(
            'pending',
            'approved',
            'rejected',
            name='user_project_status'
        ),
        default='pending'
    )

class Message(db.Model):
    """Message model for storing messages."""
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(
        db.Enum('unread', 'read', name='message_status'),
        default='unread'
    )

class Rating(db.Model):
    """Rating model for storing project ratings."""
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    rated_by_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    """Notification model for storing user notifications."""
    __tablename__ = 'notifications'
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(
        db.Enum('unread', 'read', name='notification_status'),
        default='unread'
    )

class ProjectSkill(db.Model):
    """Association table for project and skill."""
    __tablename__ = 'project_skills'
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.project_id'),
        primary_key=True
    )
    skill_id = db.Column(
        db.Integer,
        db.ForeignKey('skills.skill_id'),
        primary_key=True
    )

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    author = relationship("User", backref="posts", lazy=True)

    """
    def __repr__(self):
        return f"<Post {self.id} - {self.title}>"
    """

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"