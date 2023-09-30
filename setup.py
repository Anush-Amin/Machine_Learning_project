from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements=file_obj.readlines() 
        # there will be \n in every element of list hence we need to replace it
        requirements=[req.replace("\n", "") for req in requirements]
        # remove "-e ." from the requirements list
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

# meta-data info of the project
setup(
    name='mlproject',
    version='0.0.1',
    author='Anush Amin',
    author_email='anush.mlore@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)   