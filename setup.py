from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A basic GUI package for pygame'
LONG_DESCRIPTION = 'Simple GUI package that adds buttons, links, menus, input boxes, sliders, and more to be added'

# Setting up
setup(
    name="pygame-gui",
    version=VERSION,
    author="Praneeth Jain",
    author_email="<praneethjain005@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'pygame', 'gui'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)