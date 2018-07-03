from flask import Flask, render_template, url_for
app = Flask(__name__)

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

''' To run the script directly, I setted this function
    ONLY FOR THE DEVELOPMENT PROCESS'''
if __name__ == '__main__':
    app.run(debug=True)