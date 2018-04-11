#!/usr/bin/python3
# setup.py: uses selenium to log into holberton account using username and
# password provided by the user at the command line.

# ------------
# Introduction
# ------------

# Get project ID, username, and password
print()
print('~~~ Holberton Project Setup ~~~')
print('-' * 31)
print('Project #: ', end='')
project_id = input()
print('Student ID: ', end='')
username = input()
from getpass import getpass
password = getpass('Password: ')
print('Attempting to log in to the intranet. Just a moment...')

# ------------------------
# Selenium webdriver stage
# ------------------------

# If you want to watch the browser, change visibile parameter from 0 to 1
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800,600))
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
    print('Attempting to find project #{}'.format(project_id), end='. ')
    print('Just a moment...')

# Navigate to the project we want to generate files for
driver.get('https://intranet.hbtn.io/projects/{}'.format(project_id))
project_html = driver.find_element_by_xpath('.//html')
if 'The page you were looking for doesn\'t exist' in project_html.text:
    print('{} is not a valid project :('.format(project_id))
    exit()

# Get the content from the project's html
content = ''.join(project_html.text)

# -------------------
# File creation stage
# -------------------

# Saving the content in a file called 'project_content' in user's cwd
with open('project_content', 'w') as f:
    f.write(content)

# Create the directory for the project
import os
from parser import directory, all_files

# Store cwd for cleanup purposes
cwd = os.getcwd()

if not os.path.exists(directory):
    print('Found project #{}!'.format(project_id))
    os.makedirs(directory)
print('Creating directory: {}'.format(directory))

# Moving into that directory
os.chdir(directory)

# Creating all the files
for file in all_files:
    print('Creating file: {}'.format(file))
    with open(file, 'w', encoding='utf-8') as task:
        task.close()
print('All files created successfully!')

# -------
# Cleanup
# -------

# Remove 'project_content' file
os.chdir(cwd)
try:
    os.remove('project_content')
except OSError:
    pass

# Remove __pycache__ dir
from shutil import rmtree
rmtree('__pycache__', ignore_errors=True)

# stop display and kill selenium webdriver
driver.quit()
display.stop()

# ------------------
# Additional options
# ------------------
os.chdir(directory)
print('Would you like all files to be executable? (y/n) ')
mode = input()
if mode.lower() == 'y':
    from subprocess import run
    run('chmod u+x *', shell=True)
    print('All files are now executable!')

print('Would you like a README.md? (y/n) ')
readme = input()
if readme.lower() == 'y':
    with open('README.md', 'w', encoding='utf-8') as readme:
        readme.write('##{}\n'.format(directory))
    print('README.md created successfully!')
print('Have fun with your project!')
