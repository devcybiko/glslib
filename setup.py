from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="glslib",
    version="0.1.0",
    author="Greg",
    description="A Python package for graphics and simulation utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/glslib",
    packages=find_packages(),
    install_requires=[
        "munch>=2.5.0",
        "json5>=0.9.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
