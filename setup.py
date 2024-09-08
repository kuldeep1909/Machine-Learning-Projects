# this file is most important for the project because by this our whole 
# project can be converted into a pypi packages and we can post this

from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    This funciton will return the list of requirements 
    
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements= [req.replace('\n',"")for req in requirements]
        

    return requirements


setup(
    name= 'mlproject',
    version='0.0.1',
    author='Kuldeep Malviya',
    author_email='malviyakuldeep38@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)