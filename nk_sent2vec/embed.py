''' wrapper functions for the sent2vec model object '''

from typing import List

import sent2vec

from .config import MODEL_PATH

model = sent2vec.Sent2vecModel()
model.load_model(MODEL_PATH)


def embed_sentence(sentence: str):
    return model.embed_sentences(sentence)


def embed_sentences(sentences: List[str]):
    return model.embed_sentences(sentences)


def train_model(input_path, output_path):
    # TODO
    pass


def nearest_neighbors(query_sentence, corpus_path):
    # ./fasttext nnSent model.bin corpora [k]
    # TODO
    pass


def analogies(query_sentence, corpus_path):
    # ./fasttext analogiesSent model.bin corpora [k]
    # TODO
    pass
