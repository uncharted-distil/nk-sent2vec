from nk_sent2vec import Sent2Vec
import numpy as np

test_sentence = "this is a test"
test_sentences = ["this is a test", "this is only a test"]
model_path = "/root/models/torontobooks_unigrams.bin"


def test_doc_embedding():
    s2v = Sent2Vec(model_path)
    output = s2v.embed_sentence(test_sentence)
    print("single shape:", output.shape)
    assert isinstance(output, np.ndarray)
    assert output.ndim == 2
    assert output.shape[0] == 1

    outputs = s2v.embed_sentences(test_sentences)
    print("multi shape:", outputs.shape)
    assert isinstance(outputs, np.ndarray)
    assert outputs.ndim == 2
    assert outputs.shape[0] == 2
