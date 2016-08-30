# roles={
# 	'user':(follow|comment|write,True),
# 	'administrator':(follow|read|wirte,False)

from functools import wraps
from flask.ext.login import current_user

class Permission(object):
	follow=1
	comment=2
	write=4
	moderate=8
d=4^12 
print d

def permission_required(permission):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args,**kwargs):
			if current_user.can(permission):
				abort(403)
			return f(*args,**kwargs)
		return decorated_function
	return decorator

def admin_required(f):
	return permission_required(Permission.ADMINISTRATOR)(f)
class User(db.Model,UserMixin):
	def __init__(self,**kwargs):
		super(User,self).__init__(**kwargs)
		if self.role is None:
			if self.email==current_app.config['FLASKY_ADMIN']:
				self.role=Role.query.filter_by(permission=0xff).first()
			if self.role is None:
				self.role=Role.query.filter_by(default=True).first()

	def can(self,permissions):
		return self.role is not None and (self.permissions & permissions)==permissions
	def is_administrator(self):
		return self.can(Permission.ADMINISTER)
