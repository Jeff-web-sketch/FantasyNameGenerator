from setuptools import setup, find_packages

setup(
    name="fantasy_name_generator",
    version="1.0.0",
    description="A library for generating fantasy names (Dragons, Elves, etc.)",
    author="Jeff",
    url="https://github.com/jeff-web-sketch/FantasyNameGenerator",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "fantasy_names=cli:main",
        ],
    },
    python_requires=">=3.6",
)   
