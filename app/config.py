class Config:
    '''
    General configuration parent class
    '''
    NEW_API_BASE_URL = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey={}'

    #https://api.themoviedb.org/3/movie/{}?api_key={}
    #https://newsapi.org/v2/everything?domains=wsj.com&apiKey={}
   

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
