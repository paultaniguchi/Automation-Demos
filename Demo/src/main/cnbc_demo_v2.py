'''
cnbc_demo_v2.py
This program searches for the Dow Jones Index from https://www.cnbc.com search bar
On the Dow Jones Index graph page, it switches to 3 month view
and takes a screenshot

Structured as Page Object Model

@author: Paul Taniguchi
'''
from selenium import webdriver
from pages.home_page import HomePage

if __name__ == '__main__':
    
    test_url = 'https://www.cnbc.com/'
    test_stock = 'Dow Jones Industrial Average'
    
    # create a new Chrome session
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get(test_url)
    
    homepage = HomePage(driver)
    dow_chart = homepage.search.searchFor(test_stock)
    dow_chart.take_screenshot()
    
    driver.quit()