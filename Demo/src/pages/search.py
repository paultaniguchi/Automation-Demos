'''
Used with cnbc_demo_v2.py
Object for the search bar at the top of each page

@author: Paul Taniguchi
'''
from pages.base import BasePage
from pages.chart_page import ChartPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class SearchRegion(BasePage):
    '''
    The search bar at the top of each page
    '''
    _search_button = 'i.icon-search'
    _search_field = 'input.SearchEntry-suggestNotActiveInput'
    # assemble XPATH by concat _search_list var with term
    _search_list_beg = '//span[text()="'
    _search_list_end = '"]'

    def __init__(self, driver):
        '''
        use parent class constructor
        '''
        super(SearchRegion, self).__init__(driver)
        

    def searchFor(self, term):
        ''' searchFor enters term into the search bar to do a search
            It returns the search result list
        '''
        
        # click in the search button to open search box
        search_button = WebDriverWait(self.driver,timeout=30).until(
            expected_conditions.element_to_be_clickable(
            self.driver.find_element(By.CSS_SELECTOR,self._search_button)))
        search_button.click()

        # enter term in the search field
        search_box = WebDriverWait(self.driver,timeout=30).until(
            expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR,self._search_field)))
        search_box.clear()
        search_box.send_keys(term)
        search_box.submit()
        
        # click the term from the search list
        term_link = WebDriverWait(self.driver,timeout=30).until(
            expected_conditions.element_to_be_clickable(
                self.driver.find_element(By.XPATH,\
            ''.join([self._search_list_beg,term,self._search_list_end]))))
        term_link.click()
        
        return ChartPage(self.driver)
    
    
    

        