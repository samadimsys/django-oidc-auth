# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-oidc-auth',
    version='0.1.0',
    description='OpenID Connect client for Django applications',
    long_description='WIP',
    author='Lucas S. Magalhães',
    author_email='lucas.sampaio@intelie.com.br',
    packages=find_packages(exclude=['*.tests']),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[
        'Django>=4.2,<4.3',
        'pyjwkest>=1.4.2,<1.5',
        'requests>=2.31.0,<3',
    ],
    zip_safe=True
)
