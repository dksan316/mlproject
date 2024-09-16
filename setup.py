from setuptools import find_packages,setup
from typing import List

hu = "-e ."

def pack_requirements(file_path:str)->List[str]:
    '''
    this function will return the list
    of requirements from the given file path

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hu in requirements:
            requirements.remove(hu)

    return requirements



setup(
    name = 'mlproject',
    version = '1.0',
    author = 'Dikshant',
    author_email = 'dikshant7711@mbmcsit.edu.np',
    packages = find_packages(),
    install_requires = pack_requirements('requirements.txt')
)