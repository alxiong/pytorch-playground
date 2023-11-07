from setuptools import setup, find_packages

setup(
    name="pytorch-playground",
    version="1.0.0",
    author="Aaron Chen",
    author_email="aaron.xichen@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "quantize=quantize:main",
        ]
    },
)
