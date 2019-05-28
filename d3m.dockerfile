FROM registry.datadrivendiscovery.org/jpl/docker_images/complete:ubuntu-bionic-python36-v2019.5.8

ENV HOME=/root

WORKDIR $HOME

# install nk_sent2vec
COPY . $HOME/
# RUN python3 setup.py install 
# RUN pip3 install .
RUN pip3 install -e git+https://github.com/NewKnowledge/nk-sent2vec@master#egg=nk_sent2vec

# check that it runs by triggering tests
CMD ["pytest", "--color=yes", "-s", "tests"]