'''
chart_page.py

Used with cnbc_demo_v2.py
Page Object for the page with the stock price chart

@author: Paul Taniguchi
'''
from pages.base import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import datetime
import time

class ChartPage(BasePage):
    '''
    Chart page object
    '''
    _chart_time_range = 'div.range-3month'
    _loading_circle = 'img.Loading-loadingImage'
    _chart = 'div.QuotePageBuilder-container'

    def __init__(self, driver):
        '''
        Constructor
        '''
        super(ChartPage, self).__init__(driver)
        
        
    def _validate_page(self, driver):
        pass
    
    def take_screenshot(self):
        '''take screenshot'''
        
        # wait for chart selection bar appears before changing time range
        time_button = WebDriverWait(self.driver,timeout=120).until(
            expected_conditions.element_to_be_clickable(
                self.driver.find_element(By.CSS_SELECTOR,self._chart_time_range)))
        time_button.click()   
    
        # wait until loading circle is gone before taking screenshot
        WebDriverWait(self.driver,timeout=60).until(expected_conditions.
            invisibility_of_element_located((By.CSS_SELECTOR,
            self._loading_circle)))
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%m%d%Y_%H%M%S')
        file_name = ''.join(["Dow_Jones",st,".png"])
        chart = self.driver.find_element(By.CSS_SELECTOR,self._chart)

        # zoom out - my computer has a small display
        self.driver.execute_script("document.body.style.zoom = '0.8'")
        chart.screenshot(file_name)
        