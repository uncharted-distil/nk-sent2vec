# FROM registry.datadrivendiscovery.org/jpl/docker_images/complete:ubuntu-artful-python36-devel-20180419-092215
FROM python:3.6-slim
# FROM ubuntu:16.04

ENV HOME=/app

WORKDIR $HOME

RUN apt-get update && apt-get install -y \
    git \
    build-essential 

# copy files that define dependencies so we can have package installs in a separate image layer 
COPY requirements.txt $HOME/
# install required packages on pypi
RUN pip install -r requirements.txt

# Install set2vec: clone from git repo, compile binary, then install python bindings
RUN git clone https://github.com/epfml/sent2vec.git $HOME/sent2vec \
    && rm -rf $HOME/sent2vec/.git* \
    && cd $HOME/sent2vec \
    && make \
    && cd $HOME/sent2vec/src \
    && python setup.py build_ext \
    && pip install . 

# install nk_sent2vec
COPY . $HOME/
RUN python setup-dev.py install 

# check that it runs by triggering tests
CMD ["pytest", "--color=yes", "-s", "nk_sent2vec/tests.py"]
