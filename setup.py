from setuptools import setup
import re

readme = ""
with open('README.md') as f:
	readme = f.read()

requirements = ["pymongo","dnspython","motor"]

setup(name='Mase-DB',
      version='1.0.3',
      description='''Легкое использование базы данных монгодб''',
      url='https://github.com/MaseZev/discord-ext-dashboard',
      packages=['masedb.func'],
      license='mit',
      author="MaseZev",
      author_email='csgomanagement1',
      long_description=readme,
      install_requires=requirements,
      python_requires='>=3.7',
      zip_safe=True)
