# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read_file(filename, mode='r'):
    with open(filename, mode) as f:
        for line in f:
            yield line.strip()


def get_version():
    return read_file('VERSION.txt').next()


def get_install_requires():
    requires = []
    links = []
    for line in read_file('requirements/base.txt'):
        parts = line.split('#egg=')
        if len(parts) == 2:
            links.append(line)
            requires.append(parts[1])
        else:
            requires.append(line)
    return requires, links

install_requires, dependency_links = get_install_requires()


def get_long_description():
    with open('README.rst', 'r') as f:
        return f.read()


setup(
    name='nitrate',
    version=get_version(),
    description='Test Case Management System',
    long_description=get_long_description(),
    author='Nitrate Team',
    maintainer='Chenxiong Qi',
    maintainer_email='qcxhome@gmail.com',
    url='https://github.com/Nitrate/Nitrate/',
    license='GPLv2+',
    keywords='test case',

    install_requires=install_requires,
    dependency_links=dependency_links,

    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('/etc/httpd/conf.d/', ['contrib/conf/nitrate-httpd.conf']),
        ('/etc/init.d', ['contrib/script/celeryd']),
        ],

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
