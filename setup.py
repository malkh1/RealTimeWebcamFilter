from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='RealTimeWebcamFilter',
    version='1.0',
    packages=find_packages('src'),  # Automatically find packages under src
    package_dir={'': 'src'},        # Specify that src is the root package directory
    install_requires=requirements,
    authors='Mohammad Alkhaledi, James Anderson',
    authors_email='mohammad.alkhaledi@carleton.ca, james.anderson@carleton.ca',
    description='A lightweight program for applying a filter to live webcam footage',
    url='https://github.com/malkh1/RealTimeWebcamFilter',
    classifiers=[
        # List of classifiers (metadata) for your project (e.g., maturity, license, etc.)
        'Programming Language :: Python :: 3'
    ],
)
