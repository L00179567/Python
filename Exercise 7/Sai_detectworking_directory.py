##############
OS utilities
By: Sai Mahesh
09 DEC 2023
##############

import os, platform

# Define global variables
current_working_directory = None

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

def detect_working_directory()->str:
    # Returns the directory this script was run from
    return os.getcwd()

if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    # Check the OS in use, upper case
    my_os = detect_os()
    my_os = my_os.upper()
    
    # Parse the response, only check for Windows and Ubuntu
    if my_os == "Windows":
        print("Your system is Windows")
    elif my_os == "Ubuntu":
        print("Your system is Ubuntu")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    # Get current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")
