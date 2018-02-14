# -*- coding: utf-8 -*-
from setuptools import setup,find_packages

setup(
    name='temp-sms-watcher',
    version='2.0',
    url='https://github.com/jzarca01/temp-sms-watcher',
    license='MIT License',
    author='Jeremie Zarca',
    author_email='jeremie.zarca@gmail.com',
    keywords='temporary sms watcher',
    description=u'Module to check temporary number for received SMS',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests','lxml'],
)
