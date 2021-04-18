import unittest
from app.models import news_Source

class news_SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news_Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = news_Source(1,'Daniel Cooper','The numbers are going up but not very much','Fox News Today','https://www.cnbc.com/2019/07/26/us-gdp-second-quarter-2019.html','https://image.cnbcfm.com/api/v1/image/105712425-1564087321969welding.jpg','2019-07-26','Growth decelerated in the second quarter but not by as much as Wall Street thought')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,news_Source))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_source.newsid,1)
        self.assertEquals(self.new_source.author,'Daniel Cooper')
        self.assertEquals(self.new_source.title,'The numbers are going up but not very much')
        self.assertEquals(self.new_source.description,'Fox News Today')
        self.assertEquals(self.new_source.url,'https://www.cnbc.com/2019/07/26/us-gdp-second-quarter-2019.html')
        self.assertEquals(self.new_source.urlToImage,'https://image.cnbcfm.com/api/v1/image/105712425-1564087321969welding.jpg')
        self.assertEquals(self.new_source.publishedAt,'2019-07-26')
        self.assertEquals(self.new_source.content,'Growth decelerated in the second quarter but not by as much as Wall Street thought')
        