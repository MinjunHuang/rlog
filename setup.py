#!/usr/bin/env python
# coding: utf-8
import sys

from rlog import __version__

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup
    PyTest = lambda x: x

setup(
    name='rlog',
    version=__version__,
    description='Small handler and formatter for using python logging with Redis',
    url='https://github.com/lobziik/rlog',
    tests_require=['pytest>=2.5.0'],
    install_requires=['redis', 'ujson'],
    packages=['rlog'],
    cmdclass={'test': PyTest},
)