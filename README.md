# cpdupload
Python 3 library for batch upload from files

## Installation

This installation assumes you are using `conda` to create virtual environments.

From the command prompt with the folder of your cloned repository, execute the following commands (these only need to be ran once at installation time):

```
conda create -n cpdupload python=3.8
conda activate cpdupload
pip install -e .
```

## Running the package

From the root of the repo, type a command similar to the following. This will execute the costgraph. Note that the paths to the files will need to be changed for your particular folder structure.

```
python -m cpdupload
```

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

