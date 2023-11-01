'''
Page Object Model for the https://demoqa.com page

@author: Paul Taniguchi
'''
from pages.base import BasePage
from pages.element_page import ElementPage
from pages.base import InvalidPageException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class HomePage(BasePage):
    '''
    for the main page https://demoqa.com
    '''
    _element_tile = '//div[h5="Elements"]'
    _homepage_title = 'DEMOQA'
    _supp_list = ['div#fixedban','footer']

    def __init__(self, driver):
        '''
        Constructor
        '''
        super(HomePage, self).__init__(driver)
        
    def _validate_page(self):        
        
        try:
            # check the page title to check if page loaded
            WebDriverWait(self.driver,timeout=10).until(expected_conditions.\
                title_contains(self._homepage_title))
        except:
            raise InvalidPageException("Home Page not loaded")
        
    def tile_click(self, driver, tile):
        '''
        click the element tile on the homepage
        '''
        # find the tile passed thru
        if tile == 'elements':
            button = self.driver.find_element(By.XPATH,self._element_tile)
            button.click()
            return ElementPage(self.driver)
