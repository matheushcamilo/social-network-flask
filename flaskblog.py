from flask import Flask, render_template, url_for
from matplotlib.pyplot import title

app = Flask(__name__)

#Dummy list of dictionaries to simulate database call
posts = [
    {
        'author': 'Matheus Araujo',
        'title': 'Post #1',
        'content': 'First post content',
        'date_posted': 'April 4, 2022'
    },
    {
        'author': 'Joe Doe',
        'title': 'Post #2',
        'content': 'Second post content',
        'date_posted': 'April 4, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'Flask Blog')

if __name__ == '__main__':
    app.run(debug=True, port=8000)    