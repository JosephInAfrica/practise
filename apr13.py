@auth.route('/login',methods=['GET','POST'])
def log_in():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		login_user(user,form.remember_me.data)
		return redirect(request.args.get('next') or url_for('main.index')