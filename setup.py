from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    descriptions='Commandline user management utility',
    long_description=readme,
    author='Alexa',
    author_email="athomsen115@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={'console_scripts': 'hr=hr.cli:main'},
)
