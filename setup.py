# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rokucli',
    version='1.0.0',
    description='Command-line control of your Roku device',
    long_description=long_description,
    author='Nick Miller',
    author_email='ncmiller@openmailbox.org',
    url='https://github.com/ncmiller/roku-cli',
    packages=find_packages(),
    install_requires=[
        'roku',
        'blessed',
    ],
    license='MIT',
    platforms=["any"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='roku cli',
    entry_points={
        'console_scripts': [
            'roku=rokucli.cli:main',
        ],
    },
)
