from setuptools import setup, find_packages
from typing import List
HYPEN = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    It removes any line that starts with '-' or is empty.
    """
    with open(file_path) as file:
        requirements = file.readlines()
    
    # Remove any line that starts with '-' or is empty
    requirements = [req.replace("\n"," ") for req in requirements]

    if HYPEN in requirements:
        requirements.remove(HYPEN)
    
    return requirements

setup(
    name = "ML-Project",
    version = "0.0.1",
    author = "teja",
    author_email = "tejak6958@gmil.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)