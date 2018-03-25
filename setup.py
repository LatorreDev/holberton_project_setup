#!/usr/bin/python3
'''
setup.py: uses selenium to log into holberton account using username and
password provided by the user at the command line.
'''

# See the magic (change visible=0 to not see)
from pyvirtualdisplay import Display
display = Display(visible=1, size=(800,600))
display.start()

# Start the webdriver and load the page
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://intranet.hbtn.io/auth/sign_in')

# Enter username and password
print('Username: ')
username = input()
from getpass import getpass
password = getpass('Password: ')

# Give the driver the username and password so it can login
driver.find_element_by_id('user_login').send_keys(username)
driver.find_element_by_id('user_password').send_keys(password)
driver.find_element_by_name('commit').click()

display.stop()
