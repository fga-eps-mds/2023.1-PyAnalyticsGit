from setuptools import setup
from setuptools.dist import Distribution

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='pyanalyticsgit',
    version='0.0.5',
    license='MIT License',
    author='Gabriel Barbosa, Jefferson Sena, Mateus Levy, Pedro Henrique, Rodrigo Fonseca, Tiago Albuquerque',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='gabrielb.alencarr@gmail.com, jeffersonsena12144@gmail.com, mateuslevy06@gmail.com, pedrolulhenrique@gmail.com, Rodrigofonseca399@gmail.com, tiago28973@gmail.com ',
    keywords='pyAnalyticsGit',
    description=u'Biblioteca PyAnalyticsGit para gerar relatórios Git.',
    packages=['pyanalyticsgit', 'pyanalyticsgit/repo'],
    install_requires=['matplotlib==3.7.1', 
                      'python-dotenv==1.0.0',
                      'Requests==2.31.0',
                      'setuptools==59.6.0',
                      'wordcloud==1.9.2'],)
