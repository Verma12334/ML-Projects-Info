from setuptools import find_packages,setup
from typing import List

HYPEN_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
       
    return requirements 


setup(
    name='ML Project',
    version='0.0.1',
    author='Saurabh',
    author_email='saurabh620488@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','pandas']

)