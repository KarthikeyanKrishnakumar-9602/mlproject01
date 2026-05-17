from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(filepath:str) -> List[str]:
    '''
    To get requirements from requirements file
    '''
    requirements=[]

    with open(filepath) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject01',
    version='0.1',
    author='Karthik',
    description='A machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)