## Holberton Project Setup
**Automation tool for Holberton School projects**

- Tired of typos in your file names that lead to missed checks?
- Tired of forgetting to make a README?
- Tired of your files not being executable?

This tool does all the initial work of setting up your project so you can avoid
those mistakes and save yourself some time.

### Installation
`git clone https://github.com/eightlimbed/holberton_project_setup.git`

### Usage
After cloning this repo, simply run `./hps.py`.

You will me prompted to enter the Project # (found in the project's URL),
Student ID, and password. The script will do the rest. After creating the files
you will be prompted again for two additional options: Whether or not you want a
README, and whether or not you want your files to be executable.

![Step 1](images/hps1.png)

The new directory will be created in your current working directory and it will
be full of all files required for the mandatory tasks.

![Step 2](images/hps2.png)

Then, if needed, you can `mv the_directory where_you_want_it`.

### Notes
- I currently don't recommend using this for the bigger projects like
  `AirBnb_clone`. I've noticed some bugs with projects that involve making extra
directories, so be warned. Nothing terrible will happen to your system, but the
script might break.
- `hps.py` depends on `parser.py`, so be careful if you move these files around.
- Your README.md will only contain the name of the directory. You should add
  more to it :)

### Bugs?
Please message me here on github if you notice any bugs :)

### Want to contribute?
Message me here or on slack if you want to make this thing better :)
