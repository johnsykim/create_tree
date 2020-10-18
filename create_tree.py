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