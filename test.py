from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Set the ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 

#Initialize the driver
driver = webdriver.Chrome('/root/selenium/chromedriver', chrome_options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

# Set the target for the driver 
driver.get('http://myappdynamics.local:8090/controller/#/location=AD_HOME_OVERVIEW') 
# Wait for the redirection / 
time.sleep(120)

#This is just an example how to list elements on the page
ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    print ii.tag_name
    print ii.get_attribute('id')    # id name as string

driver.save_screenshot('screenshot.png')
username = driver.find_element_by_id("userNameInput")
password = driver.find_element_by_id("passwordInput")

username.clear()
password.clear()

username.send_keys("Username")
time.sleep(1)

password.send_keys("Password")
time.sleep(1)


#Check in the screen whether all the input fields are properly filled
driver.save_screenshot('screenshot2.png')

#Click on the Login button
driver.find_element_by_id("submitInput").click()

#Wait for the login
time.sleep(30)

#Check the home screen
driver.save_screenshot('screenshot7.png')
