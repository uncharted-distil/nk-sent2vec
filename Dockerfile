FROM registry.datadrivendiscovery.org/jpl/docker_images/complete:ubuntu-artful-python36-v2018.6.5

ENV HOME=/nk_sent2vec

WORKDIR $HOME

# install nk_sent2vec
COPY . $HOME/
RUN python3 setup.py install 

# check that it runs by triggering tests
CMD nosetests
