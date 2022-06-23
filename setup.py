from setuptools import setup
from typing import List


#Declaring variables for stup functions
PROJECT_NAME="Housing-predictor"
VERSION="0.0.1"
AUTHOR="Mohit Nikumbh"
DESCRIPTION="This fsds batch first machine learning project."
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


#def function which read requirements file and return list of strings
def get_requirements_list()->List[str]:
    """
    Discription: This function is going to return list of requirement 
    mention in requirement.txt file

    return this function is going to return list which will contain name of libraries 
    mentioned in requirements.txt file 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    
    

setup(name = PROJECT_NAME,
version = VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages=PACKAGES,
install_requires =get_requirements_list() )




    


