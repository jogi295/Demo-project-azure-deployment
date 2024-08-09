from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "DEMO-PROJECT-DEPLOY"
VERSION = "0.0.1"
DESCRIPTION = "Demo project for deployment"
AUTHOR_NAME = "JOGI"
AUTHOR_EMAIL = "jogeswararaon@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.strip() for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
