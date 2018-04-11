#!/usr/bin/python3
# parser.py: Goes through the content of the project page and gets the GitHub
# Repository, Directory Name, and File Names

github_repo, directory, file_names, project_name = ([],[],[],[])

with open('project_content', 'r', encoding='utf-8') as content:
    for line in content:
        if line.startswith('0x'):
            project_name.append(line)
        if line.startswith('GitHub repository: '):
            github_repo.append(line)
        if line.startswith('Directory: '):
            directory.append(line)
        if line.startswith('File: '):
            file_names.append(line)

# Getting GitHub Repo
try:
    github_repo = list(set(github_repo))[0].split(' ')[2][0:-1]
except IndexError:
    print('Something went wrong. Make sure you entered the correct project ID')
    exit()

# Getting Directory
directory = list(set(directory))[0].split(' ')[1][0:-1]

# Getting File Names
file_names = set(file_names)

# Some tasks require multiple files
clean_names, multi_files = ([],[])
for file in file_names:
    if ',' in file:
        multi_files.append(file)
    else:
        clean_names.append(file.split('File: ')[1])

cleaner_names = []
for file in clean_names:
    cleaner_names.append(file[0:-1])

cleaner_multi_files, super_clean_multi_files = ([],[])
for file in multi_files:
    cleaner_multi_files.append(file.split('File: ')[1])
for file in cleaner_multi_files:
    subfiles = file.split(', ')
    for file in subfiles:
        super_clean_multi_files.append(file)
pristine_multi_files = []
for file in super_clean_multi_files:
    if '\n' in file:
        pristine_multi_files.append(file[0:-1])
    else:
       pristine_multi_files.append(file)

all_files = []
for file in pristine_multi_files:
    all_files.append(file)
for file in cleaner_names:
    all_files.append(file)

# Finally...
all_files = sorted(all_files)
