#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages

setup(
    name='agentics',
    version='1.2.1-post3',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='The 80s DOS game re-written in Python',
    long_description=open('./README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rolphs/TheStockWolf',
    packages=find_packages(),
    install_requires=[
        'terminaltables',
        'pyyaml'
    ],
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'agentics = agentics.__main__:main',
            'stockwolf = stockwolf.main:cli',
            'stockwolf-game = integration.game_loop:cli'
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Games/Entertainment :: Turn Based Strategy'
    ]
)
