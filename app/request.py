from app import app
import urllib.request,json
from .models import new

New = new.New

# Getting api key
api_key = app.config['NEW_API_KEY']

# Getting the movie base url
base_url = app.config["NEW_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)


    return new_results

def process_results(new_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        title = new_item.get('title')
        name = new_item.get('name')
        author = new_item.get('author')
        description= new_description.get('description')
        content = new_content.ge('content')

        if poster:
            new_object = New(id,title,name,author, description, content)
            new_results.append(new_object)

    return new_results

def get_new(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None
        if new_details_response:
            id = new_details_response.get('id')
            title = new_details_response.get('original_title')
            name = new_details_response.get('name')
            author = new_details_response.get('author')
            description = new_details_response.get('description')
            content = new_details_response.get('content')

            new_object = New(id,title ,name,author, description, content)

    return new_object

def search_new(new_name):
    search_new_url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={}'.format(api_key,new_name)
    with urllib.request.urlopen(search_new_url) as url:
        search_new_data = url.read()
        search_new_response = json.loads(search_new_data)

        search_new_results = None

        if search_new_response['results']:
            search_new_list = search_new_response['results']
            search_new_results = process_results(search_new_list)


    return search_new_results