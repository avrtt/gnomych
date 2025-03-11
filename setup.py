from setuptools import setup, find_packages

setup(
    name="gnomych",
    version="1.0.0",
    description="Advanced data cleaning & validation system for automated data cleaning, validation, profiling and correction suggestions.",
    author="Vladislav Averett",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "jsonschema>=3.0.0",
        "scikit-learn>=0.22.0"
    ],
    entry_points={
        "console_scripts": [
            "gnomych=gnomych.__main__:main"
        ]
    },
)