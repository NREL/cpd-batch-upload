# cpdupload
Python 3 library for batch upload from files

## Installation

This installation assumes you are using `conda` to create virtual environments.

From the command prompt with the folder of your cloned repository, execute the following commands (these only need to be ran once at installation time):

```
conda create -n cpdupload python=3.9
conda activate cpdupload
pip install -e .
```

## Running the package

```
python -m cpdupload --input [CSV or JSON input filename] --api [base URL of CPD API]
```

## Building the documentation

First, there is a lot of documentation in docstrings throughout the `cpdupload` package. Second, this documentation is gathered into an easily navigable form with the Sphinx documentation builder. You can build the `.html` files for the documentation with the following commands from the root of the repo on macOS

``` 
cd docs
make clean
make html
```

After those commands finish you can open the documentation in the `docs/_build/html/index.html` file.

## Guide for development

### Code formatting and type checking

To ensure code consistency, we use MyPy for type checking and Black for code formatting. This table lists some information on these packages and how they are set up:

Package | What it does | Configuration File | URL for more information |
---|---|---|---
MyPy | Creates optional type checking for variables in the code to reduce errors that arise from type mismatches | `mypy.ini` | [http://mypy-lang.org/](http://mypy-lang.org/)
Black | Ensures code is consistently formatted | `pyproject.toml` | [https://black.readthedocs.io/en/stable/](https://black.readthedocs.io/en/stable/)

### Manually executing code formatting and type checking

From the root of the repo, run the following commands

```
mypy cpdupload
black cpdupload
```

If all passes, you will get status messages that look similar to the following:

The message from MyPy:

```
Success: no issues found in 1 source file
```

The message from Black:

```
All done! ✨ 🍰 ✨
1 file left unchanged.
```

Black has the useful feature that, if it finds a non-compliant file, it will fail with an error but will also reformat the file for you.

The first time you run MyPy can be slow since it needs to parse the files and put them into a cache for faster type checking.

