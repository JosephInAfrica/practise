from flask.ext.login import UserMixin,AnonymousUserMxin
class Permission:
	FOLLOW=0x01
	COMMENT=0x02
	WRITE_ARTICLES=0x04
	MODERATE_COMMENTS=0x08
	ADMINISTER=0x80

@main.route('user/<username>',methods=['GET','POST'])
def user(username):
	user=User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template( )
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

		}
		for r in roles:
			role=Role.query.filter_by(name=r).first()
			if role is None:
				role=Role(name=r)
			role.permissions=roles[r][0]
			role.defualt=roles[r][1]
			db.session.add(role)
		db.session.commit()

class User(db.Model,UserMixin):
	def __init__(self,**kwargs):
		super(self).__init__(**kwargs)
		if self.role is None:
			if self.email==current_app.config['FLASKY_ADMIN']:
				self.role=Role.query.filter_by(permissions=0xff).first()
			if self.role is None:
				self.role=Role.query.filter_by(defualt=True).first()

	def can(self,permissions):
		return self.role is not None and (self.role.permissions&permissions) ==permissions
	def is_administrator(self):
		return self.can(Permission.ADMINISTER)

class AnonymousUser(AnonymousUserMxin):
	def can(self,permissions):
		return False
	def is_administrator(self):
		return False
@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permission)