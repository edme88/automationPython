# automationPython
Automation test with Python and Selenium

### How to start?
Remember to download chromedriver.exe to a 'Drivers' folder in the root.

Run the command 
* pip install
* pip install html-testRunner
* pip install pytest-html-reporter
* pip install pytest-html

Pluing recomended: [Ranorex Selocity](https://chrome.google.com/webstore/detail/ranorex-selocity/ocgghcnnjekfpbmafindjmijdpopafoe)


### Pages to Practice
- POMDemo: Tets for http://automationpractice.com/
- Store: Test for https://automationteststore.com/


### Python test for https://automationteststore.com/
- Login Page 
  - TEST: Invalid Login - No User - No Pass
  - TEST: Valid Login - Check My Account title
    
- Register Page
  - TEST: Check message error from each field
  - TEST: Check message error: Account Alredy Exist
  - TEST: Long text - Check message error: login name not available & password not match
  
### Generate Reports
> cd Store
> cd Tests
> pytest LoginTest.py RegisterTest.py