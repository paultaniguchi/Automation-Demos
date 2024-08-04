'''
Parent class for the tests of the https://demoqa.com website

@author: Paul Taniguchi
'''
#import unittest
from selenium import webdriver


class BaseTestCase():

    _test_url = 'https://demoqa.com'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self._test_url)


    def tearDown(self):
        self.driver.quit()

