'''
home_page.py

Used by cnbc_demo_v2.py
Page Object for the https://cnbc.com page

@author: Paul Taniguchi
'''
from pages.base import BasePage
from pages.base import InvalidPageException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class HomePage(BasePage):
    '''
    home page for https://www.cnbc.com
    '''
    _home_page_tiles = 'div.MarketCard-row'


    def __init__(self, driver):
        '''
        Constructor
        '''
        super(HomePage, self).__init__(driver)
        
    def _validate_page(self):        
        
        try:
            # home page has loaded when the ome page tiles are present
            WebDriverWait(self.driver,timeout=10).until(expected_conditions.\
                visibility_of_element_located((By.CSS_SELECTOR,self._home_page_tiles)))
        except:
            raise InvalidPageException("Home Page not loaded")