'''
Page Object Model for the https://demoqa.com/elements page

@author: Paul Taniguchi
'''
from pages.base import BasePage
from pages.base import InvalidPageException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from enum import Enum

class ElementPage(BasePage):
    '''
    Elements page class
    '''

    _elementpage_url = 'elements'
    # Text Box tests
    _text_box = '//li[span="Text Box"]'
    _text_box_fields = {'name':'input#userName', 'email':'input#userEmail',
            'currentAddress':'textArea#currentAddress',
            'permanentAddress':'textArea#permanentAddress'}
    _display_fields = {'name':'p#name', 'email':'p#email',
            'currentAddress':'p#currentAddress',
            'permanentAddress':'p#permanentAddress'}
    _submit_button = 'button#submit'
    # Buttons tests
    _buttons = '//li[span="Buttons"]'
    _double_click_button = 'button#doubleClickBtn'
    _double_click_text= 'p#doubleClickMessage'
    _right_click_button = 'button#rightClickBtn'
    _right_click_text = 'p#rightClickMessage'
    _click_button = {'double':'button#doubleClickBtn','right':
                'button#rightClickBtn','single':'button#hcu9D'}
    _click_text = {'double':'p#doubleClickMessage','right':
                'p#rightClickMessage','single':'p#dynamicClickMessage'}
    # when div#fixedban is removed on home page, not necessary to
    # remove on other pages 
    _supp_list = ['div#Ad\.Plus-970x250-1','div#Ad\.Plus-970x250-2',
                  'section#RightSide_Advertisement']

    class element_button_type(Enum):
        '''
        enums representing button type
        '''
        RIGHT = 'right'
        DOUBLE = 'double'
        SINGLE = 'single'
    
    
    def __init__(self, driver):
        '''
        Constructor
        '''
        super(ElementPage, self).__init__(driver)
        
    def _validate_page(self):   
        '''
        check that it's on correct page
        '''     
        try:
            # check the page title to check if page loaded
            WebDriverWait(self.driver,timeout=10).until(expected_conditions.\
                url_contains(self._elementpage_url))
        except:
            raise InvalidPageException("Element Page not loaded")
        
    # for the Text Box page
    def go_to_text_box_page(self):
        '''
        select text_box from accordion
        '''
        self.driver.find_element(By.XPATH,self._text_box).click()
                
    def set_text_box_fields(self, text_box_data):
        '''
        put data from text_box_data into the text_bbox 
        text_box_data is a dictionary
        '''
        # expose text box
        self.go_to_text_box_page()
        
        for key in self._text_box_fields:
            text_box_field = self.driver.find_element(By.CSS_SELECTOR,self.
                            _text_box_fields[key])
            text_box_field.clear()
            text_box_field.send_keys(text_box_data[key])
            
        # submit button
        self.scroll_and_click(self.driver.find_element(By.CSS_SELECTOR,
                    self._submit_button))
            
    def get_text_box_display_fields(self):
        '''
        get the test data from the output section
        '''
        actual_display_field = dict()
        for key in self._display_fields:
            actual_display_field[key] = self.driver.find_element(By.CSS_SELECTOR,
                self._display_fields[key]).text
            
        return actual_display_field
    
    # for the Buttons page
    def go_to_click_buttons_page(self):
        '''
        select buttons from accordion
        '''
        self.driver.find_element(By.XPATH,self._buttons).click()
        
    
    def general_click_me_click(self, button_type):
        '''
        click the button_type button where
        button_type is enum DOUBLE, RIGHT, or SINGLE
        '''
        # expose click buttons
        self.go_to_click_buttons_page()
        
        click_button = WebDriverWait(self.driver,timeout=30).until(expected_conditions.\
                element_to_be_clickable((By.CSS_SELECTOR,
                                           self._click_button[button_type.value])))
        
        #if button_type == 'double':
        if button_type is self.element_button_type.DOUBLE:
            ActionChains(self.driver).double_click(click_button).perform()
        #elif button_type == 'right':
        elif button_type is self.element_button_type.RIGHT:
            ActionChains(self.driver).context_click(click_button).perform()
        else:
            ActionChains(self.driver).click(click_button).perform()

    def get_general_click_me_text(self, button_type):
        '''
        return the text that's displayed after the button_type Click Me
        button is clicked
        button_type is enum DOUBLE, RIGHT, or SINGLE
        '''
        return self.driver.find_element(By.CSS_SELECTOR,self.
                    _click_text[button_type.value]).text