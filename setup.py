#!/usr/bin/env python

"""
    edit _version.py
    python setup.py dist
    python setup.py tag
    commit/push (neccessary to update readthedocs)
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    make sure: click a link on test.pypi and install: pip install -i https://test.pypi.org/simple/ django-admin-autocomplete-all
    not required, but if I want to have docs/_build (it is git-excluded) generated: v docs: make html
    on readthedocs.org click your name(account) and (re)build docs
    twine upload dist/*
"""

import os
import re
import sys

from setuptools import setup


exec(open("autocomplete_all/_version.py").read())


if sys.argv[-1] == 'dist':  # původně: publish, volalo setup.py včetně: upload
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist')        # publish: + upload
    os.system('python setup.py bdist_wheel')  # publish: + upload
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-admin-autocomplete-all',
    version=__version__,
    description="""django admin: use select2 (autocomplete_fields) everywhere""",
    long_description=readme + '\n\n' + history,
    author='Mirek Zvolský',
    author_email='zvolsky@seznam.cz',
    url='https://github.com/pyutil/django-admin-autocomplete-all',
    download_url='https://github.com/pyutil/django-admin-autocomplete-all/archive/%s.tar.gz' % __version__,
    packages=[
        'autocomplete_all',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-admin-autocomplete-all',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
