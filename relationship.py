registrations=db.Table(
	db.Column('student_id',db.Integer,db.ForeignKey('Student.id')),
	db.Column('class_id',db.Integer,db.ForeignKey('Class.id'))
	)

class Student(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String)
	classes=db.Relationship('Class',secondary='registrations',backref=db.backref('students',lazy='dynamic'),lazy='dynamic')

class Class(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String)


class Follow(db.Model):
	follower_id=db.Column(db.Integer,ForeignKey='users.id')
	followed_id=db.Column(db.Integer,ForeignKey='users.id')
	timestamp=db.column(db.Datetime,default=datetime.utcnow)

class User(db.Model,db.UserMixin):
	follower=db.Relationship('Follow',foreign_keys=[Follow.followed_id],backref=db.backref('followed',lazy='joined'),lazy='dynamic',cascade='all,delete-orphan')
	followed=db.Relationship('Follow',ForeignKey='follower.id',backref=db.backref('follower',lazy='dynamic'),lazy='dynamic')
