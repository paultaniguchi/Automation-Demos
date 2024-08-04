'''
Tests for the Elements UI on the https://demoqa.com/elements page

@author: Paul Taniguchi
'''

from tests.base_test_case import BaseTestCase
from pages.home_page import HomePage
from pages.element_page import ElementPage
from _pytest.fixtures import fixture

class TestElementPage(BaseTestCase):
   
    @fixture
    def go_to_element_page(self):
        '''
        Starting with the home page, go to the Element page
        '''
        self.setUp()
        
        # click the Elements tile
        homepage = HomePage(self.driver)

        elementpage = homepage.go_to_page(homepage.home_page_tile.ELEMENT)

        yield elementpage

        self.tearDown()
    
    def test_text_box(self, go_to_element_page):
        '''
        enter data into form
        verify that the correct data is returned
        '''
        text_box_data = {'name':'Alan Smithee', 
                             'email':'alan.smithee@example.com',
            'currentAddress':"""123 Fake St\nCurrent City, NY, 99999""",
            'permanentAddress':"""456 Fake St\nPermanent City, NY, 99999"""}
        exp_text_box_data = {'name':'Name:Alan Smithee', 
                             'email':'Email:alan.smithee@example.com',
        'currentAddress':"""Current Address :123 Fake St Current City, NY, 99999""",
        'permanentAddress':"""Permanent Address :456 Fake St Permanent City, NY, 99999"""}
    
        go_to_element_page.set_text_box_fields(text_box_data)
        
        # test the correct user details is returned
        # note: in the actual web page Permanent is misspelled as Permananet 
        # this test will fail        
        assert go_to_element_page.get_text_box_display_fields() == exp_text_box_data
        
    def test_double_click_button(self, go_to_element_page):
        '''
        Double click the Double Click Me button
        verify that the correct text is displayed
        '''
        exp_double_click_text = 'You have done a double click'
        
        go_to_element_page.general_click_me_click(go_to_element_page
                        .element_button_type.DOUBLE)
        assert go_to_element_page.get_general_click_me_text(
            go_to_element_page.element_button_type.DOUBLE) == exp_double_click_text
        
    def test_right_click_button(self, go_to_element_page):
        '''
        Right click the Right Click Me button
        verify that the correct text is displayed
        '''
        exp_right_click_text = 'You have done a right click'
        
        go_to_element_page.general_click_me_click(go_to_element_page
                            .element_button_type.RIGHT)
        assert go_to_element_page.get_general_click_me_text(
            go_to_element_page.element_button_type.RIGHT) == exp_right_click_text
