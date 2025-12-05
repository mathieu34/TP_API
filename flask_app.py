from flask import Flask , render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'test' 
db = SQLAlchemy(app)    #connection instance mysql a la place : PyMySQL 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Register") # changer nom du bouton 

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],
                             render_kw={"placeholder": "Password"})
    submit = SubmitField("Log In") # changer nom du bouton 

class SearchForm(FlaskForm): 
    film_title = StringField(validators=[InputRequired(), Length(min=4, max=30)],
                            render_kw={"placeholder": "Film Title"})
    submit = SubmitField("Search")

class Disconnect(FlaskForm):
    submit = SubmitField("Disconnect")

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/register', methods= ['GET', 'POST'])
def register () :
    form = RegisterForm()
    if form.validate_on_submit() : 
       user = User(username=form.username.data,
                   password=form.password.data)
       db.session.add(user)
       db.session.commit()
       return redirect(url_for('login'))

    return render_template('register.html', form=form) # lien vers ton HTML


@app.route('/login', methods= ['GET', 'POST'])
def login() : 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('search'))#"Hello" #redirect(url_for('other route'))

    return render_template('login.html', form=form)


@app.route('/disconnect', methods = ['GET', 'POST'])
@login_required
def disconnect () : 
    logout_user()
    return redirect(url_for('login'))



@app.route('/search', methods= ['GET', 'POST'])
@login_required #lié à logout_user(), sécurité d'accès à la page 
def search () : 
    form = SearchForm()
    API_KEY = "7c6eca28d3d2cd801a8a05c47d28c7c4"
    movies_list = []
    if form.validate_on_submit() : 
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=fr-FR&page=1&query={form.film_title.data}"
        response = requests.get(url)
        if response.status_code == 200 : 
            response = response.json()['results']
            for movie in response : 
                for k,v in movie.items() :
                    if k == 'poster_path' : 
                        movies_list.append(v)
                 
    return render_template('search.html', form=form, movies_list=movies_list)

    

if __name__ == '__main__' : 
    with app.app_context():
        db.create_all()
        print("Tables créées :", db.inspect(db.engine).get_table_names())

    app.run(debug=True)