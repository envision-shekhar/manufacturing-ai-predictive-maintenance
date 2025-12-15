
# src/app.py
import argparse
from retriever import Retriever
from llm import answer_with_rules
from redaction import redact

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--question', type=str, required=True)
    parser.add_argument('--docs', type=str, default='docs')
    args = parser.parse_args()
    r = Retriever(args.docs)
    ctx = r.search(args.question, k=4)
    ctx = [redact(c) for c in ctx]
    ans = answer_with_rules(args.question, ctx)
    print("
Context:
" + "
---
".join(ctx))
    print("
Answer:
" + ans)
