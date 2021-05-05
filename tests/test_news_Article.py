import unittest
from app.models import news_Article
#New = new.New

class NewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        self.new_article = news_Article(1,'The numbers are going up but not very much','Fox News Today','https://www.cnbc.com/2019/07/26/us-gdp-second-quarter-2019.html','Growth decelerated in the second quarter but not by as much as Wall Street thought')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,news_Article))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.article_id,1)
        self.assertEquals(self.new_article.title,'The numbers are going up but not very much')
        self.assertEquals(self.new_article.description,'Fox News Today')
        self.assertEquals(self.new_article.articleurl,'https://www.cnbc.com/2019/07/26/us-gdp-second-quarter-2019.html')
        self.assertEquals(self.new_article.content,'Growth decelerated in the second quarter but not by as much as Wall Street thought')
        


if __name__ == '__main__':
    unittest.main()