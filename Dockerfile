FROM registry.datadrivendiscovery.org/jpl/docker_images/complete:ubuntu-artful-python36-v2018.6.5

ENV HOME=/app

WORKDIR $HOME

# install nk_sent2vec
COPY . $HOME/
# RUN python3 setup.py install 
# RUN pip3 install .
RUN pip3 install -e git+https://github.com/NewKnowledge/nk-sent2vec#egg=nk_sent2vec --process-dependency-links

# check that it runs by triggering tests
CMD nosetests
