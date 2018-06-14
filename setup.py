import os
import setuptools.command.develop as develop_cmd
import setuptools.command.install as install_cmd
from setuptools import setup

current_dir = os.path.dirname(os.path.abspath(__file__))
S2V_INSTALL_PATH = os.getenv('S2V_INSTALL_PATH', os.path.join(current_dir, 'sent2vec'))


class install(install_cmd.install):
    ''' Build sent2vec/FastText c++ binary, then pip install sent2vec. '''

    def run(self):
        install_cmd.install.run(self)
        os.system("git clone https://github.com/epfml/sent2vec.git {0}".format(S2V_INSTALL_PATH))
        os.system("cd {0} && make".format(S2V_INSTALL_PATH))
        os.system("cd {0}/src && python setup.py build_ext && pip install . ".format(S2V_INSTALL_PATH))


class develop(develop_cmd.develop):
    ''' Build sent2vec/FastText c++ binary, then pip install sent2vec. '''

    def run(self):
        develop_cmd.develop.run(self)
        os.system("git clone https://github.com/epfml/sent2vec.git {0}".format(S2V_INSTALL_PATH))
        os.system("cd {0} && make".format(S2V_INSTALL_PATH))
        os.system("cd {0}/src && python setup.py build_ext && pip install . ".format(S2V_INSTALL_PATH))


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
        'install': install,
        'develop': develop,
    }
)
