from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dceucm.policy',
      version=version,
      description="Policy for the DCE UCM website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='dce ucm',
      author='Israel Saeta',
      author_email='dukebody@gmail.com',
      url='http://www.ucm.es',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dceucm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
