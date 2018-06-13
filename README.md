# Document Embedding
A python wrapper for embedding text documents using sent2vec, which draws on FastText.

To embed a list of strings `documents`, use:

```
from doc_emb import embed_docs
embedded_docs = embed_docs(documents)
```

## Testing
Tests can be run using `nosetests`
