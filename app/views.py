from flask import render_template
from app import app

# Views
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Into the badlands'
    return render_template('index.html',message = message)

@app.route('/new/<new_id>')
def new(new_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('new.html',id = new_id)