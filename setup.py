from setuptools import setup

desc = """
pipedream:
    Useful stuff for building distributed pipelines and data workflows.
"""

install_requires = [
        "netifaces==0.8",
        "docopt==0.6.1",
        "pyzmq==14.0.1",
        "nose>=1.3.0",
        "coverage==3.7.1",
        ]

test_requires = [
        "pep8==1.4.6",
        "pylint==1.0.0",
        ]

setup(
    name="pipedream",
    packages=['pipedream', ],
    version="0.1a",
    install_requires=install_requires,
    tests_require=test_requires,
    description=desc,
    author="Kevin Murray",
    author_email="spam@kdmurray.id.au",
    url="https://github.com/borevitzlab/pipedream",
    keywords=["grid computing", "parallel", "pipeline",
        "distrubuted computing"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later " +
            "(GPLv3+)",
        ],
    test_suite="tests",
    )
