#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0.2"

if sys.argv[-1] == 'publish':
    try:
        import wheel  # noqa
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='reshell',
    version=version,
    description="""Python reverse bash shell""",
    long_description=readme + '\n\n' + history,
    author='Peter Demin',
    author_email='peterdemin@gmail.com',
    url='https://github.com/peterdemin/reshell',
    include_package_data=True,
    py_modules=['reshell'],
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords='reshell',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'reshell = reshell:main',
        ]
    },
)
