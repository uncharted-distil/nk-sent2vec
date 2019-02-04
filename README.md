# Document Embedding
A python wrapper for embedding text documents using [sent2vec](https://github.com/epfml/sent2vec), which draws on FastText.

To embed a list of strings `documents`, use:

```
from d3m_sent2vec import Sent2Vec 

vectorizer = Sent2Vec(path = '/home/nk-sent2vec/models/torontobooks_unigrams.bin')

print(vectorizer.embed_sentences(sentences=[documents]))
```

## Testing
Tests can be run using `nosetests -s`
