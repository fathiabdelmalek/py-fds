from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py-fds",
    version="3.5.3",
    author="Abdelmalek Fathi",
    author_email="abdelmalek.fathi.2001@gmail.com",
    url="https://github.com/FathiMalek/py-fds.git",
    description="Simple implementation of data structures for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pyfds', 'pyfds.utils'],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
