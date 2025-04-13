from setuptools import find_packages,setup
from typing import List

hypen_e = '-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        requirement = file.readlines()
        requirement = [i.replace('\n','') for i in requirement]

        if hypen_e in requirement:
            requirement.remove(hypen_e)
    return requirement


setup(
    name = 'text_summarising',
    version = '0.0.1',
    author = 'vardhman_ajmera',
    author_email = 'vardhmanajmera76@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)