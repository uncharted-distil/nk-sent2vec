import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class InstallSent2Vec(install):
    ''' Build sent2vec FastText binary, then pip install sent2vec. '''

    def run(self):
        # os.system("pip install -r requirements.txt")
        os.system("cd nk_sent2vec/sent2vec && make")
        os.system("cd nk_sent2vec/sent2vec/src && python setup.py build_ext && pip install . ")
        install.run(self)


class DevelopSent2Vec(develop):
    ''' Build sent2vec FastText binary, then pip install sent2vec. '''

    def run(self):
        os.system("cd nk_sent2vec/sent2vec && make")
        os.system("cd nk_sent2vec/sent2vec/src && python setup.py build_ext && pip install . ")
        install.run(self)


setup(
    name='nk_sent2vec',
    version='1.0.0',
    description='Embeds text documents using sent2vec',
    author='New Knowledge',
    packages=['nk_sent2vec'],
    package_data={'': ['*.h, *.cc', '*Makefile']},
    include_package_data=True,
    install_requires=[
        'Cython>=0.28.3',
        'numpy>=1.14.1',
        'nose>=1.3.7',
    ],
    cmdclass={
        'install': InstallSent2Vec,
        'develop': DevelopSent2Vec,
    }
)
