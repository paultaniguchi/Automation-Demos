'''
Parent class for the pages on the https://demoqa.com website.

@author: Paul Taniguchi
'''
from abc import abstractmethod
from selenium.webdriver.common.by import By

class BasePage(object):
    '''
    Base class for the pages
    '''
    # hide footer in parent class; it will be overridden
    _supp_list = ['footer']

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
        self._validate_page()
        
    @abstractmethod
    def _validate_page(self):
        return
    
    def suppress_ad_banner(self, driver):
        '''
        hide pesky ad banners by changing DOM visibility
        see https://stackoverflow.com/questions/49921128/selenium-cant-click-element-because-other-element-obscures-it
        '''
        for supp_css in self._supp_list:
            ad_element = self.driver.find_element(By.CSS_SELECTOR, 
                                                  supp_css)
            self.driver.execute_script("arguments[0].setAttribute\
            ('style',arguments[1]);",ad_element, "visibility:hidden;")
            
    
class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass