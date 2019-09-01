from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='pdf_downloader',
    version='0.0.9',
    url='https://github.com/lambdaofgod/pdf_downloader',
    author='Jakub "lambdaofgod" Bartczuk',
    author_email='bartczukkuba@gmail.com',
    packages=find_packages(),
    install_requires=requirements
)