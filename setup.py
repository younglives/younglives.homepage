from setuptools import setup, find_packages
import os

version_path = os.path.join("younglives", "homepage", "version.txt")

version = open(version_path).read().strip()

long_description = open(os.path.join("docs", "README.txt")).read()
long_description += "\n" + open(os.path.join("docs", "INSTALL.txt")).read()
long_description += "\n" + open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='younglives.homepage',
      version=version,
      description="",
      long_description=long_description,
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='',
      author='Michael Davis',
      author_email='m.r.davis@cranfield.ac.uk',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['younglives'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.OrderableReferenceField',
          'Products.Carousel',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
