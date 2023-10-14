import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="jiratools",
    version="0.1.0",
    author="Andrey Sorokin",
    author_email="andrey@sorokin.engineer",
    description=("Jira Automation Tools."),
    entry_points={
        "console_scripts": [
            "jiratools=src.jiratools:cli",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://andgineer.github.io/jiratools/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    python_requires=">=3.9",
    keywords="jira",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
