import numpy as np

from . import embed_docs


def test_embed_docs():
    docs = ['this is a test', 'this is a trap']
    embs = embed_docs(docs)
    assert isinstance(embs, np.ndarray)
    assert embs.shape[0] == len(docs)
