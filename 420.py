from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatrureSerizlizer as Serializer
from markdown import markdown
import bleach
from flask import current_app,request
from flask.ext.login import UserMixin,AnonymousUserMixin
from . import db,login_manager

class Permission:
	FOLLOW=0x01
	COMMETN=0x02
	WRITE_ARTICLES=0x04
	MODERATE_COMMENTS=0x08
	ADMINISTER=0x80

class Role(db.Model):
	__tablename__='roles'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	default=db.Column(db.Boolean,default=False,index=True)
	permissions=db.Column(db.Integer)
	users=db.relationship('User',backref='role',lazy='dynamic')
	@staticmethod
	def insert_roles():
		roles={
		'User':(Permission.FOLLOW|Permission.COMMENT|PERMISSION.WRITE_ARTICLES,True),
		'Moderator':(Permission.FOLLOW|Permission.COMMENT|Permission.WRITE_ARTICLES|PERMISSION>MODERATE+COMMENTS,False),
		'Administrator':(0xff,False)
		}
		for r in roles:
			role=Role.query.filter_by(name=r).first()
			if role is None:
				role=Role(name=r)
			role.permissions=roles[r][0]
			role.default=roles[r][1]
			db.session.add(role)
		db.session.commit()

	def __repr__(self):
		return '<Role %r>'%self.name

class Follow(db.Model):
	__tablename='follows'
	follower_id=db.Column(db.Integer,db.Foreignkey('users.id'),primary_key=True)
	followed_id=db.Column(db.Integer,db.ForeignKey('users.id'),primary_key=True)
	timestamp=db.Column(db.DateTime,default=datetime.utcnow)

class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(64),unique=True,index=True)
	username=db.Column(db.String(64),unique=True,index=True)
	role_id=db.Column(db.Integer,db.ForeignKey())
	password_hash=db.Column(db.Integer,db.ForeignKey('roles.id'))
	confirmed=db.Column(db.Boolean,default=False)
	name=db.Column(db.String(64))
	location=db.Column(db.String(64))
	about_me=db.Column(db.Text())
	member_since=db.Column(db.DateTime(),default=datetime.utcnow)
	last_seen=db.Column(db.DateTime(),default=datetime.utcnow)
	avatar_hash=db.Column(db.String(32))

	posts=db.relationship('Post',backref='author',lazy='dynamic')
	
	followed=db.relationship('Follow',foreign_keys=[Follow.follower_id],backref=db.backref('follower',lay='joined'),lazy='dynamic',cascade='all,delete-orphan')

	follower=db.relationship('Follow',Foreign_keys=[Follow.follwed_id],backref=db.backref('followed',lazy='joined'),lazy='dynamic',cascade='all,delete-orphan')

	comments=db.relationship('Comment',backref='author',lazy='dynamic')

	@staticmethod
	def generate_fake(count=100):
		from sqlalchemy.exc import IntegrityError
		from random import seed
		import forgery_py

		seed()
		for i in range(count):
			u=User(email=forgery_py.internet.email)





