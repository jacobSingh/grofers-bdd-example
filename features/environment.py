# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os

def set_up_selenium():
	if (os.getenv("GROFERS_BDD_LOCAL")):
		driver = webdriver.Safari()
		driver.set_window_size(1290, 960)
		driver.set_window_position(0, 0)
	else:
		# This is the only code you need to edit in your existing scripts.
        	# The command_executor tells the test to run on Sauce, while the desired_capabilities
        	# parameter tells us which browsers and OS to spin up.
		desired_cap = {
			'platform': "Mac OS X 10.9",
			'browserName': "chrome",
			'version': "31",
		}
		username = os.getenv('SAUCE_USERNAME')
		access_key = os.getenv('SAUCE_ACCESS_KEY')
		driver = webdriver.Remote(
			command_executor='http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(username, access_key),
			desired_capabilities=desired_cap)
    
	return driver

def before_scenario(context):
	context.driver = set_up_selenium()

def after_scenario(context):
	context.driver.quit()
