from setuptools import setup

setup(
    name="gherkin-official",
    packages=["gherkin", "gherkin.pickles", "gherkin.stream"],
    version="29.0.0",
    description="Gherkin parser (official, by Cucumber team)",
    long_description="Gherkin parser (official, by Cucumber team)",
    author="Cucumber Ltd and Björn Rasmusson",
    author_email="cukes@googlegroups.com",
    url="https://github.com/cucumber/gherkin",
    license="MIT",
    download_url="http://pypi.python.org/pypi/gherkin-official",
    keywords=["gherkin", "cucumber", "bdd"],
    scripts=["bin/gherkin"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    platforms=["any"],
    package_data={"gherkin": ["gherkin-languages.json"]},
    install_requires=[
        "typing_extensions>=4",
    ],
    python_requires=">=3.8",
)
