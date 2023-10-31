'''
base.py

Parent class for the https://cnbc.com pages

@author: Paul Taniguchi
'''
from abc import abstractmethod

class BasePage(object):
    '''
    parent class for the page objects
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver        
        self._validate_page()

        
    @abstractmethod
    # abstract for checking the page
    def _validate_page(self):
        return
    
    # search is present on all pages
    @property
    def search(self):
        from pages.search import SearchRegion
        return SearchRegion(self.driver)
    
# exception to be thrown when page doesn't load
class InvalidPageException(Exception):
        pass