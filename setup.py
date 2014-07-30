from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='iod-python',
      version=version,
      description="IDOL OnDemand python client library",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='IDOL idolondemand iod',
      author='Martin Zerbib',
      author_email='martinzerbib@gmail.com',
      url='http://idolondemand.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'requests'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
