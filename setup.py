from setuptools import setup

setup(
    name="py-todo",
    version="0.1.0",
    packages=["src"],
    entry_points={"console_scripts": ["py-todo = src.__main__:main"]},
)
