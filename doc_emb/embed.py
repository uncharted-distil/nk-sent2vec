from typing import List

import sent2vec

from .config import MODEL_PATH

model = sent2vec.Sent2vecModel()
model.load_model(MODEL_PATH)


def embed_docs(docs: List[str]):
    return model.embed_sentences(docs)
