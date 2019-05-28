import os
from distutils.core import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


current_dir = os.path.dirname(os.path.abspath(__file__))
S2V_INSTALL_PATH = os.getenv("S2V_INSTALL_PATH", os.path.join(current_dir, "sent2vec"))
# S2V_INSTALL_PATH = "/root/epfml_sent2vec"


def install_sent2vec():
    # Clone epfml's sent2vec repo, build sent2vec FastText binary, and pip install sent2vec.
    os.system("pip3 install -r requirements.txt")
    os.system(f"git clone https://github.com/epfml/sent2vec.git {S2V_INSTALL_PATH}")
    # os.system(
    #     f"cd {S2V_INSTALL_PATH} && git reset --hard 392428b294a6da9c91b6e705c14b8e2e408e34a7"
    # )
    os.system(f"cd {S2V_INSTALL_PATH} && make")
    os.system(f"cd {S2V_INSTALL_PATH} && python3 setup.py build_ext && pip3 install . ")


class InstallSent2Vec(install):
    # Build sent2vec FastText binary, then pip install sent2vec.

    def run(self):
        install_sent2vec()
        install.run(self)


class DevelopSent2Vec(develop):
    def run(self):
        install_sent2vec()

        develop.run(self)


setup(
    name="nk_sent2vec",
    version="1.2.1",
    description="Embeds text documents using sent2vec",
    author="New Knowledge",
    packages=["nk_sent2vec"],
    package_data={"": ["*.h, *.cc", "*Makefile"]},
    include_package_data=True,
    install_requires=["Cython", "numpy", "pytest"],
    cmdclass={"install": InstallSent2Vec, "develop": DevelopSent2Vec},
)
