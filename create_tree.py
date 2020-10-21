# Author: John Sangyeob Kim
# Date Created: 2019-09-16
# Last Updated: 2019-09-23
# Note: Automatically create project subdirectories and update history of project metadata

"""
  This program automatically creates project subdirectories and updates history of project metadata. Its interface is designed to be user-friendly: before processing, it asks you to prepare the following information:

  - Desired working directory
  - Project name
  - # of collaborators and their IDs
  - # of subprojects

  You are also allowed to quit the program at anytime by typing and entering 'q'. Once you provide all information, the program will utilize the user-defined parameters to create project subdirectories.

  Each lowest-level folder (.../project/coce/user/subproject/) will contain three template codes ('0_main.py', '1_task.py', and '2_task.py') which are duplicates of 'template_code.py'. The names and the template are customizable.

  Every time the program runs, it updates 'metadata_history.txt', which contains the root directory, program run date, and the user-defined parameters.
"""

# Import packages and define template_code and template_item
import os, shutil
pwd = os.getcwd()
template_code = pwd/'template_code.py'
template_item = ['0_main.py', '1_task.py', '2_task.py']

# Override input function so that the user can abort the program at anytime
__original_input = input
def input(*args, **kwargs):
  res = __original_input(*args, **kwargs)
  if res == "q":
    print("aborting the program...\n"+"********************************************")
    exit()
  else:
    return res

# Welcome statement
print("*********************************************************************\n"
  + "Welcome! You're about to create your new project.\n"
  + "Before you proceed, you'll need the following information:\n"
  + "- Desired working directory\n"
  + "- Project name\n"
  + "- # of collaborators and their IDs\n"
  + "- # of subprojects\n"
  + "To quit this program at anytime, type \"q\" and press Enter \n"
  + "*********************************************************************")

# Ask if the user is ready
while True:
  ready = input("Are you ready? [y/n] ")
  if ready == 'y':
    print("Let's begin.")
    break
  elif ready == 'n':
    print("That's okay. I'll see you later.")
    exit()
  else:
    print("Please type either \"y\" or \"n\".")
    continue