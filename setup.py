import os
from setuptools import setup


def read(fname):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="huh",
    version="0.0.2",
    author="Param Singh",
    author_email="me@param.codes",
    description="A tool to help you understand error messages.",
    license="MIT",
    keywords="ai llm openai error messages",
    url="https://github.com/paramsingh/huh",
    packages=['huh'],
    scripts=["huh/huh"],
    long_description=read('README.md'),
    install_requires=[
        'click',
        'keyring',
        'openai',
        'yaspin',
        'click-default-group',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
