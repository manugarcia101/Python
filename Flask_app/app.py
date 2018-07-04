from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c697a01af2a682894c85665364ef21d0' #SECRET KEY TO AVOID XSS

post = [
    {
        'author': 'Manu Garcia',
        'title': 'First python web',
        'content': 'First content',
        'date_posted': 'July 03, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog',
        'content': 'Second content',
        'date_posted': 'July 04, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = post)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About us')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print('Hola q packa')
    print(str(form))
    if form.validate_on_submit():
        print('Hola q ase')
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

''' To run the script directly, I setted this function
    ONLY FOR THE DEVELOPMENT PROCESS'''
if __name__ == '__main__':
    app.run(debug=True)