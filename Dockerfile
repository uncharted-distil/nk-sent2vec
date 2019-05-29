FROM continuumio/miniconda3:4.5.11

ENV HOME=/root
WORKDIR $HOME

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential

COPY environment.yml $HOME/
RUN conda update -n base conda && \
    conda env update -f $HOME/environment.yml

RUN git clone https://github.com/epfml/sent2vec.git && \
    cd sent2vec && \
    make && \
    python setup.py build_ext && \
    pip install . 

COPY . $HOME/

RUN pip install -e .

CMD ["pytest", "--color=yes", "-s", "tests"]