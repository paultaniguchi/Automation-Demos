'''
Tests for the Elements UI on the https://demoqa.com/elements page

@author: Paul Taniguchi
'''
from tests.base_test_case import BaseTestCase
from pages.home_page import HomePage
import unittest

class ElementPageTest(BaseTestCase):

    _elements_tile = 'elements'

    def test_text_box(self):
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
    
        # click the Elements tile
        homepage = HomePage(self.driver)
        homepage.suppress_ad_banner(self.driver)
        elementpage = homepage.tile_click(self.driver, self._elements_tile)
        elementpage.suppress_ad_banner(self.driver)
        # bring up the Text Box UI & fill out field
        elementpage.click_text_box(self.driver)
        elementpage.set_text_box_fields(self.driver, text_box_data)
        
        # test the correct user details is returned
        # note: in the actual web page Permanent is misspelled as Permananet 
        # this test will fail        
        self.assertDictEqual(elementpage.get_text_box_display_fields(self.driver),
                             exp_text_box_data)
        
    def test_double_click_button(self):
        '''
        Double click the Double Click Me button
        verify that the correct text is displayed
        '''
        exp_double_click_text = 'You have done a double click'
        
        # click the Elements tile
        homepage = HomePage(self.driver)
        homepage.suppress_ad_banner(self.driver)
        elementpage = homepage.tile_click(self.driver, self._elements_tile)
        elementpage.suppress_ad_banner(self.driver)
        # bring up the Buttons UI
        elementpage.click_buttons(self.driver)
        elementpage.general_click_me_click(self.driver,'double')
        self.assertEqual(elementpage.get_general_click_me_text(self.driver,'double'),
                exp_double_click_text)
        
    def test_right_click_button(self):
        '''
        Right click the Right Click Me button
        verify that the correct text is displayed
        '''
        exp_right_click_text = 'You have done a right click'
        
        # click the Elements tile
        homepage = HomePage(self.driver)
        homepage.suppress_ad_banner(self.driver)
        elementpage = homepage.tile_click(self.driver, self._elements_tile)
        elementpage.suppress_ad_banner(self.driver)
        # bring up the Buttons UI
        elementpage.click_buttons(self.driver)
        elementpage.general_click_me_click(self.driver,'right')
        self.assertEqual(elementpage.get_general_click_me_text(self.driver,'right'),
                exp_right_click_text)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=3)