from setuptools import setup, find_packages
setup(
    name="port",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages("src", exclude="test")
)
