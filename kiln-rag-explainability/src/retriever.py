
# src/retriever.py
import os, glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, docs_dir: str):
        self.paths = sorted(glob.glob(os.path.join(docs_dir, '*.txt')))
        texts = [open(p, 'r', encoding='utf-8').read() for p in self.paths]
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.matrix = self.vectorizer.fit_transform(texts)
        self.texts = texts
    def search(self, query: str, k: int = 4):
        q = self.vectorizer.transform([query])
        sims = cosine_similarity(q, self.matrix)[0]
        idxs = sims.argsort()[::-1][:k]
        return [self.texts[i][:1000] for i in idxs]
