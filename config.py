import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources?country=us&apiKey={}'

    #https://api.themoviedb.org/3/movie/{}?api_key={}
    #https://newsapi.org/v2/everything?domains=wsj.com&apiKey={}
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
        pass
   

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

app_config = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'config' : Config,
}