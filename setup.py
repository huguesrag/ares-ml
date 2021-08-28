from setuptools import find_packages, setup

setup(
    name='ares',
    packages=find_packages(include=['ares']),
    version='0.1.0',
    description='Python library to speed up boring processing stuff - for Data Science/ML',
    author='Hugues Raguenes',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
)