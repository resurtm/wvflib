#!/usr/bin/env python

from setuptools import setup

from wvflib import version


def readme():
    with open('README.rst') as f:
        return f.read()


download_url = 'https://github.com/resurtm/wvflib/archive/v{version}.tar.gz'
download_url = download_url.format(version=version)

setup(
    name='wvflib',
    version=version,
    description='Wavefront OBJ Files Loader/Saver',
    long_description=readme(),
    url='https://github.com/resurtm/wvflib',
    download_url=download_url,
    author='resurtm',
    author_email='resurtm@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
    ],
    packages=['wvflib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'coverage',
    ],
)
