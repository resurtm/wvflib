#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='wvflib',
    version='0.0.1',
    description='Wavefront OBJ Files Loader/Saver',
    long_description=readme(),
    url='https://github.com/resurtm/wvflib',
    download_url='https://github.com/resurtm/wvflib/archive/v0.0.1.tar.gz',
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
