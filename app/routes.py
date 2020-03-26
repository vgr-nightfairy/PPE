from flask import render_template, flash, redirect, url_for, request, Blueprint
from werkzeug.urls import url_parse
from app.extensions import db
from app.forms import LoginForm, RegistrationForm, MaskForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Mask


server_bp = Blueprint('main', __name__)


@server_bp.route('/')
@server_bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', user=current_user)


@server_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@server_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@server_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


## Pushes form data for N95 Masks to database
## Refer to Excel for datatype clarification
@server_bp.route('/masks', methods=['GET', 'POST'])
@login_required
def masks():
    form = MaskForm()
    if form.validate_on_submit():
        mask = Mask(
            authority=current_user.username,
            brand=form.brand.data,
            size=form.size.data,
            number=form.number.data,
            item_number=form.item_number.data,
            daily_use=form.daily_use.data,
            projected_daily_use=form.projected_daily_use.data,
            projected_run_out=form.projected_run_out.data,
            comments=form.comments.data
        )
        db.session.add(mask)
        db.session.commit()
        flash('You have submitted an update for N95 Masks of brand ' + form.brand.data + '.')
        return redirect(url_for('main.masks'))
    return render_template('masks.html', title='N95 Masks', form=form)
