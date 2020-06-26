#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        'Click>=7.0', 
        'mailjet-rest',
        ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Óscar García Población",
    author_email='oscar.garcia@makingscience.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Some tools arround the official mailjet-rest to add speciallized django views and utils",
    entry_points={
        'console_scripts': [
            'i2_django_mailjet=i2_django_mailjet.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='i2_django_mailjet',
    name='i2_django_mailjet',
    packages=find_packages(include=['i2_django_mailjet', 'i2_django_mailjet.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/opobla/i2_django_mailjet',
    version='0.0.1',
    zip_safe=False,
)
