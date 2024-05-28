from my_app import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.Text(200))
    profile_picture = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    skills = db.relationship('Skill', secondary='User_skills')
    projects = db.relationship('Project', secondary='User_projects')

class Message(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum('unread', 'read', name='message_status'), default='unread')
    user = db.relationship('User', secondary='User_id')

class Skill(db.Model):
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

class Rating(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    rated_by_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    __tablename__ = 'notifications'
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum('unread', 'read', name='notification_status'), default='unread')

class UserSkill(db.Model):
    __tablename__ = 'user_skills'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)

class ProjectSkill(db.Model):
    __tablename__ = 'project_skills'
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)

class UserProject(db.Model):
    __tablename__ = 'user_projects'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), primary_key=True)
    role = db.Column(db.Enum('owner', 'member', 'collaborator', name='user_project_role'), default='member')
    status = db.Column(db.Enum('pending', 'approved', 'rejected', name='user_project_status'), default='pending')
    rating = db.relationship('Rating', secondary='rating_id')