from setuptools import setup
from setuptools.dist import Distribution

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='pyanalyticsgit',
    version='0.2',
    license='MIT License',
    author='Jefferson Sena',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='jeffersonsena12144@gmail.com',
    keywords='Py Analytics Git',
    description=u'Biblioteca PyAnalyticsGit para gerar relatórios Git.',
    packages=['analyticsgit'],
    install_requires=['requests'],)