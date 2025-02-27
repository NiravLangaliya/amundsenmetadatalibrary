# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import os

from setuptools import find_packages, setup

__version__ = '3.3.0'


requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='amundsen-metadata',
    version=__version__,
    description='Metadata service for Amundsen',
    url='https://www.github.com/amundsen-io/amundsenmetadatalibrary',
    maintainer='Amundsen TSC',
    maintainer_email='amundsen-tsc@lists.lfai.foundation',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
        ('git+https://www.github.com/hilearn/marshmallow-'
         'annotations.git@a7a2dc96932430369bdef36555082df990ed9bef#egg=marshmallow-annotations')
    ],
    install_requires=[
        'marshmallow>=3.0,<=3.6',
        'marshmallow-annotations'
    ],
    extras_require={
        'oidc': ['flaskoidc==0.1.1']
    },
    python_requires=">=3.6",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
