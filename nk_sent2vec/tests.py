''' Tests for nk_sent2vec '''
import numpy as np

from . import embed_sentences, model, train_model, nearest_neighbors, analogies


def test_embed_sentences():
    docs = ['this is a test', 'this is a trap']
    embs = embed_sentences(docs)
    print(embs)
    print(embs.shape)
    assert isinstance(embs, np.ndarray)
    assert embs.shape == (len(docs), model.get_emb_size())


def test_train_model():
    train_model('input_path', 'output_path')


def test_nearest_neighbors():
    nearest_neighbors('query_sentence', 'corpus_path')


def test_analogies():
    analogies('query_sentence', 'corpus_path')
