from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads the requirements from the specified file and returns them as a list of strings.
    """

    requirement_list = []
    try:
        with open('requirements.txt', 'r') as f:
            # Read the contents of the file
            lines = f.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines, comments and -e .
                if requirement and not requirement.startswith('#') and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"File not found: requirements.txt")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return requirement_list


setup(
    name='NetworkSecurity',
    description='A project for network security using machine learning',
    version='0.1',
    author='Habeeb O. Issa',
    author_email='habeebissa023@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)