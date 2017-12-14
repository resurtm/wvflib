#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from wvflib import version


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        cov.stop()
        sys.exit(errcode)


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
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
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
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    platforms='any',
)
