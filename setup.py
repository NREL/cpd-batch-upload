import setuptools

name = "cpdupload"
version = "0.0.1"

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author="Alicia Key",
    author_email="alicia.key@nrel.gov",
    description="Python library for interface to Catalyst Property Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["cpdupload"],
    install_requires=[
        "pytest",
        "mypy",
        "black",
        "sphinx",
        "pandas",
        "sphinx-rtd-theme",
        "boto3",
        "warrant",
        "PyYAML"
    ]
)
