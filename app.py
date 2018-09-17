from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://developer:developer@127.0.0.1:8889/enamail'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(500), unique=True)
    description = db.Column(db.String(280), unique=True)

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def __repr__(self):
        return '<Video %r>' % self.name


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    guardian_1_name = db.Column(db.String(100), unique=False)
    guardian_1_phone = db.Column(db.String(15), unique=False)
    guardian_1_email = db.Column(db.String(100), unique=True)
    guardian_2_name = db.Column(db.String(100), unique=False)
    guardian_2_phone = db.Column(db.String(15), unique=False)
    guardian_2_email = db.Column(db.String(100), unique=True)

    def __init__(self, name, guardian_1_name, guardian_1_phone, guardian_1_email, guardian_2_name, guardian_2_phone,
                 guardian_2_email):
        self.name = name
        self.guardian_1_name = guardian_1_name
        self.guardian_1_phone = guardian_1_phone
        self.guardian_1_email = guardian_1_email
        self.guardian_2_name = guardian_2_name
        self.guardian_2_phone = guardian_2_phone
        self.guardian_2_email = guardian_2_email

    def __repr__(self):
        return '<Patient %r>' % self.name


@app.route('/')
def index():
    return render_template('add_patient.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post_video', methods=['POST'])
def post_video():
    video = Video(request.form['title'], request.form['url'], request.form['description'])
    db.session.add(video)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post_patient', methods=['POST'])
def post_patient():
    patient = Patient(request.form['name'], request.form['guardian_1_name'],request.form['guardian_1_phone'], request.form['guardian_1_email'], request.form['guardian_2_name'], request.form['guardian_2_phone'], request.form['guardian_2_email'])
    db.session.add(patient)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
