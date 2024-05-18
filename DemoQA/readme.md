## DemoQA

Automated tests for the website https://demoqa.com.  This uses the Selenium library to control a local Firefox browser.

# What does it do?
- elements_test.py goes to the Elements page and executes unit tests for the following widgets:
    - Tests that right-clicking the button triggers the correct text
    - Tests that double-clicking the button triggers the correct text.
    - Tests submitting an address into the text entry box

## Dependencies
 - Selenium
 - Pytest
 
## Files
### Tests
```
src/tests
    base_test_case.py
    elements_test.py
```
### Page Object Models
```
src/pages
    base.py
    element_page.py
    home_page.py
```
