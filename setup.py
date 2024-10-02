from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clibb",
    version="0.3.0",
    description="CLIBB (Command-Line Interface Building Blocks) streamlines, simplifies and speeds up your CLI creation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dreamfarer",
    url="https://github.com/Dreamfarer/clibb",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
