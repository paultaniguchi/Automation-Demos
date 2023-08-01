'''

This program searches for the Dow Jones Index from https://www.cnbc.com search bar
On the Dow Jones Index graph page, it switches to 3 month view
and takes a screenshot

@author: Paul Taniguchi
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import datetime, time

if __name__ == '__main__':

    # create a new Chrome session
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("https://www.cnbc.com/")

    # wait for tiles to load - so search box is active
    WebDriverWait(driver,timeout=60).until(expected_conditions.
    visibility_of_element_located((By.CSS_SELECTOR,'div.MarketCard-row')))
    
    # click in the search button to open search box
    search_button = WebDriverWait(driver,timeout=30).until(expected_conditions.
    element_to_be_clickable(driver.find_element(By.CSS_SELECTOR,'i.icon-search')))
    search_button.click()

    # Search for Dow in the search field
    search_box = WebDriverWait(driver,timeout=30).until(expected_conditions.
    visibility_of_element_located((By.CSS_SELECTOR,'input.SearchEntry-suggestNotActiveInput')))
    search_box.clear()
    search_box.send_keys("Dow Jones Industrial Average")
    search_box.submit()
    
    # select DJIA from the search results
    # only XPATH seems to work for picking out the DJIA link
    DJ_link = WebDriverWait(driver,timeout=30).until(expected_conditions.
    element_to_be_clickable(driver.find_element(By.XPATH,
            '//span[text()="Dow Jones Industrial Average"]')))
    DJ_link.click()
    
    # wait for chart selection bar appears before changing time range
    time_button = WebDriverWait(driver,timeout=120).until(expected_conditions.
    element_to_be_clickable(driver.find_element(By.CSS_SELECTOR,'div.range-3month')))
    time_button.click()   
    
    # wait until loading circle is gone before taking screenshot
    WebDriverWait(driver,timeout=60).until(expected_conditions.
    invisibility_of_element_located((By.CSS_SELECTOR,'img.Loading-loadingImage')))
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%m%d%Y_%H%M%S')
    file_name = ''.join(["Dow_Jones",st,".png"])
    #file_name = "Dow_Jones" + st + ".png"
    chart = driver.find_element(By.CSS_SELECTOR, 'div.QuotePageBuilder-container')

    # zoom out - my computer has a small display
    driver.execute_script("document.body.style.zoom = '0.8'")
    chart.screenshot(file_name)
    
    # close browser
    driver.quit()