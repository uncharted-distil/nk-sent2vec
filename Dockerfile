FROM python:3.6

ENV HOME=/app

WORKDIR $HOME

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    git \
    unzip \
    g++ \
    make \
    cmake \
    && rm -rf /var/cache/apk/*

RUN git clone https://github.com/epfml/sent2vec.git /sent2vec \
    && rm -rf /sent2vec/.git* \
    && cd /sent2vec \
    && make 

COPY requirements.txt $HOME/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt 

RUN cd /sent2vec/src \
    && python setup.py build_ext \
    && pip install . 

COPY . $HOME/