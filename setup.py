#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='python-ms5837',
      version='1.0.1',
      description='A Python3 library for the Blue Robotics MS5837 Bar30 and Bar02 pressure/temperature sensor',
      author='Blue Robotics',
      url='https://www.bluerobotics.com/',
      install_requires=[
            'smbus2',
      ],
      packages=find_packages()
      )
