from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    requirement_list:List[str] = []
    try:
        with open("requirement.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
            print("Requirement.txt file not found")
    
    return requirement_list



setup(
     name="network_security",
     version="0.0.1",
     author="Rounak Kumar",
    author_email= "rounakgupta914@gmail.com",
    packages= find_packages(),
    install_requires = get_requirement()
    
)