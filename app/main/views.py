from flask import render_template , request , redirect , url_for
from ..request import get_news_source , get_news_sources
from ..models import news_Article
from . import main


# Views
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general = get_news_sources('general')
    business = get_news_sources('business')
    technology = get_news_sources('technology')
    health = get_news_sources('health')
    science = get_news_sources('science')
    sports = get_news_sources('sports')
   
    title = 'This is new'

    search_news_source = request.args.get('news_query')

    if search_news_source:
        return redirect(url_for('main.index',news_name = search_news_source))
    else:
        return render_template('index.html',title = title,general = general ,business = business, technology = technology,health=health,science=science,sports=sports)

@main.route('/new/<int:id>')
def new(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    source = get_news_source(id)
    newsid = id.capitalize()
    title = f'{newsid}'
    details = id.capitalize()
    content = f'{details}'
    # articles = news_source.get_news_source(source.id)
    return render_template('news_source.html',  title = title, id = newsid ,source = source ,content = content)
n render_template('new.html',title = title,new = new)

@main.route('/search/<movie_name>')
def search(new_name):
    '''
    View function to display the search results
    '''
    new_name_list = new_name.split(" ")
    new_name_format = "+".join(new_name_list)
    searched_news= search_new(new_name_format)
    title = f'search results for {new_name}'
    return render_template('search.html',news = searched_news)

