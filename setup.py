#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='cieloApi3',
    version='0.1.7',
    description='SDK API-3.0 Python Cielo',
    author='Charles Tenorio da Silva',
    author_email='charlestenorios@gmail.com',
    url='https://github.com/CharlesTenorio/API-3.0-Python',
    keywords='api3.0 cielo python sdk ecommerce',
    packages=find_packages(),
    install_requires=['requests', 'future'],
    license='MIT',
    classifiers=(
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Pytest',
    )
)


setup(**settings)




# # -*- coding: utf-8 -*-
# from setuptools import setup

# setup(
#     name='cieloApi3',
#     version='0.1.1',
#     url='',
#     license='MIT License',
#     author='Thiago Malaquias',
#     author_email='',
#     keywords='api3.0 cielo python sdk ecommerce',
#     description=u'',
#     packages=['cielo.api30'],
#     install_requires=['requests'],
# )
