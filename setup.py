# -*- coding: utf-8 -*-

import unittest

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


def vcr_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name='vcr',
    version='0.0.8',
    description='VCR - decorator for capturing and simulating network ' +
                'communication',
    long_description=readme,
    author='The ObsPy Development Team',
    author_email='devs@obspy.org',
    url='https://github.com/obspy/vcr',
    download_url='https://github.com/obspy/vcr/archive/master.zip',
    license="GNU Lesser General Public License",
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='setup.vcr_test_suite',
    setup_requires=['future'],
    tests_require=['requests'],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 ' +
            '(LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
)
