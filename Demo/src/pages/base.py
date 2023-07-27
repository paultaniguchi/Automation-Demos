'''
base.py

Parent class for the https://cnbc.com pages

@author: Paul Taniguchi
'''
from abc import abstractmethod

class BasePage(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self._validate_page(driver)
        self.driver = driver
        
    @abstractmethod
    # abstract for checking the page
    def _validate_page(self, driver):
        return
    
    # search is present on all pages
    @property
    def search(self):
        from pages.search import SearchRegion
        return SearchRegion(self.driver)
    
# exception to be thrown when page doesn't load
class InvalidPageException(Exception):
        pass