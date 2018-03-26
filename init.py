#!/usr/bin/python3
# setup.py: uses selenium to log into holberton account using username and
# password provided by the user at the command line.

# Get project ID, username, and password
print('Holby File Generator')
print('-' * 19)
print('Project #: ', end='')
project_id = input()
print('Username: ', end='')
username = input()
from getpass import getpass
password = getpass('Password: ')
print('Attempting to log in to the intranet...')

# See the magic (change visible=0 to not see)
from pyvirtualdisplay import Display
display = Display(visible=1, size=(800,600))
display.start()

# Start the webdriver and load the page
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://intranet.hbtn.io/auth/sign_in')

# Give the driver the username and password so it can login
driver.find_element_by_id('user_login').send_keys(username)
driver.find_element_by_id('user_password').send_keys(password)
driver.find_element_by_name('commit').click()

# Check if login succeeded
html = driver.find_element_by_xpath('.//html')
if 'Invalid' in html.text:
    print('Invalid username/id or password :(')
    exit()
else:
    print('Login successful!')
    print('Attempting to find project #{}'.format(project_id))

# Navigate to the project we want to generate files for
driver.get('https://intranet.hbtn.io/projects/{}'.format(project_id))
project_html = driver.find_element_by_xpath('.//html')
if 'The page you were looking for doesn\'t exist' in project_html.text:
    print('{} is not a valid project :('.format(project_id))
    exit()
else:
    print('Found project #{}!'.format(project_id))

# Getting the content from the project's html
content = ''.join(project_html.text)

# Saving the content in a file called 'c0nt3nt'
# I'll delete this when I'm done
with open('c0nt3nt', 'w') as f:
    f.write(html)

from parser import project_name
print('Generating files for {}'.format(project_name))
print('...')

driver.close()
display.stop()
