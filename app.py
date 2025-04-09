from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models import db, User, Job, Application  # <-- importing db and models from models.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'

# ✅ Initialize database with app
db.init_app(app)

# ✅ Setup Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'],
                    password=request.form['password'],
                    role=request.form['role'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'employer':
        jobs = Job.query.filter_by(posted_by=current_user.id).all()
        return render_template('dashboard.html', jobs=jobs)
    elif current_user.role == 'jobseeker':
        applications = Application.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', applications=applications)
    return render_template('dashboard.html')

@app.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'employer':
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            description=request.form['description'],
            salary=request.form['salary'],
            location=request.form['location'],
            company=request.form['company'],
            posted_by=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('post_job.html')

@app.route('/apply/<int:job_id>')
@login_required
def apply(job_id):
    if current_user.role != 'jobseeker':
        return redirect(url_for('dashboard'))
    application = Application(user_id=current_user.id, job_id=job_id)
    db.session.add(application)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
