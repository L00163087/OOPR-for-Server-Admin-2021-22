"""
# 
# File          : __init__.py.py
# Created       : 27-09-2021 02:24 PM
# Author        : Varnit Rohilla
# Version       : v1.0.0
# Licensing     : (c) 2021 Varn R., LYIT
#                  Avaialable under GNU license Policy
#             
"""
if __name__ == '__main__':
    '''

   Main method of application 



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''

# importing the standard modules of python to fetch the sys, os and related information from the machine

import os
import platform
import sys


def details():
    # Machine Details
    python_path = sys.exec_prefix
    print("\nThe path in which the current file is present : " + python_path)
    python_version = sys.path[5]
    print("The python version used in my system: " + python_version[17:len(python_version)])

    print("Owner of the PC : " + os.environ["USERNAME"])

    print("Name of the machine : " + platform.node())

    print("Processor in the machine :  : " + platform.machine())

    print("Version of the Operating system is : " + platform.system() + " " + platform.release())


if __name__ != '__main__':
    pass
else:
    details()
