from setuptools import setup

setup(
    name="fig-cli",
    version="1.0",
    description="A simple CLI tool that prints ASCII text using pyfiglet, shortcut to print pyfiglet",
    py_modules=["fig"],
    install_requires=["pyfiglet"],
    entry_points={
        "console_scripts": [
            "fig=fig:main"
        ]
    },
)