# Minimal RAG stub — chunk, embed (hash), retrieve
import hashlib
docs=["YasirLab builds ML systems","RAG retrieves relevant chunks","LLM generates answers"]
def embed(s): return int(hashlib.md5(s.encode()).hexdigest()[:8],16)%100
def retrieve(q): return sorted(docs, key=lambda d: abs(embed(d)-embed(q)))[:2]
print(retrieve("What does YasirLab build?"))
