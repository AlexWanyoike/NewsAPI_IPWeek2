from flask import render_template
from app import app
from .request import get_news, get_new, search_new

# Views
# Views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    print(popular_news)
   
    title = 'This is new'
    return render_template('index.html', title = title,popular = popular_news)

@app.route('/new/<int:id>')
def new(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    new = get_new(id)
    title = f'{new.title}'

    return render_template('new.html',title = title,new = new)

@app.route('/search/<movie_name>')
def search(new_name):
    '''
    View function to display the search results
    '''
    new_name_list = new_name.split(" ")
    new_name_format = "+".join(new_name_list)
    searched_news= search_new(new_name_format)
    title = f'search results for {new_name}'
    return render_template('search.html',news = searched_news)

