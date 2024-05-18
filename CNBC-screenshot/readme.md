# CNBC-screenshot

Scripts for taking a screenshot of the Dow Jones Industrial Average 3-month
chart from https://cnbc.com.  This uses the Selenium library to control a local Chrome browser.  Screenshots are PNG images with the filename format: Dow_JonesMMDDYYYY_hhmmss.png.

# What does it do?

 - cnbc_demo_v1.py enters "DJIA" into the search field on the home page.  It takes a screenshot of the 3-month chart.  To run:
 
```
python -m cnbc_demo_v1
```
 - cnbc_demo_v2.py does the same thing as cnbc_demo_v1.py except it uses the Page Object Model structure.  To run:
 
```
python -m cnbc_demo_v2
```

## Files
### Main files
```
src\main
    cnbc_demo_v1.py
    cnbc_demo_v2.py
```
### Page Object Model
```
src\pages
    base.py
    chart_page.py
    home_page.py
    search.py
```