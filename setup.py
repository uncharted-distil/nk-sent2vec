import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

<<<<<<< HEAD
S2V_INSTALL_PATH = '/app/epfml_sent2vec'


class InstallSent2Vec(install):
    ''' Build sent2vec FastText binary, then pip install sent2vec. '''

    def run(self):
        os.system("pip3 install -r requirements.txt")
        os.system("git clone https://github.com/epfml/sent2vec.git {0}".format(S2V_INSTALL_PATH))
        os.system("cd {0} && make".format(S2V_INSTALL_PATH))
        os.system("cd {0}/src && python3 setup.py build_ext && pip3 install . ".format(S2V_INSTALL_PATH))
        install.run(self)


class DevelopSent2Vec(develop):
    ''' Clone epfml's sent2vec repo, build sent2vec FastText binary, and pip install sent2vec. '''

    def run(self):
        os.system("pip3 install -r requirements.txt")
        os.system("git clone https://github.com/epfml/sent2vec.git {0}".format(S2V_INSTALL_PATH))
        os.system("cd {0} && make".format(S2V_INSTALL_PATH))
        os.system("cd {0}/src && python3 setup.py build_ext && pip3 install . ".format(S2V_INSTALL_PATH))
        develop.run(self)
=======

class PostDevelopCommand(develop):
    ''' Build sent2vec FastText binary, then pip install sent2vec. '''

    def run(self):
        os.system("git clone https://github.com/epfml/sent2vec.git")
        os.system("cd sent2vec && make")
        os.system("cd sent2vec/src && python3 setup.py build_ext --old_and_unmanageable && pip3 install . ")
        install.run(self)


class PostInstallCommand(install):
    ''' Build sent2vec FastText binary, then pip install sent2vec. '''

    def run(self):
        os.system("git clone https://github.com/epfml/sent2vec.git")
        os.system("cd sent2vec && make")
        os.system("cd sent2vec/src && python3 setup.py build_ext --old_and_unmanageable && pip3 install . ")
        install.run(self)
>>>>>>> b008b17f7920d6a831e27bac10af95f9af1ec436


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
