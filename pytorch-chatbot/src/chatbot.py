# Minimal seq stub — shows tokenization + training loop structure
import torch, torch.nn as nn
vocab={"hello":0,"hi":1,"bye":2,"<unk>":3}
def tokenize(s): return [vocab.get(w,3) for w in s.lower().split()]
class ChatRNN(nn.Module):
    def __init__(self, vocab=4, emb=8, hid=16):
        super().__init__()
        self.emb=nn.Embedding(vocab,emb)
        self.rnn=nn.GRU(emb,hid,batch_first=True)
        self.fc=nn.Linear(hid, vocab)
    def forward(self,x): e=self.emb(x); _,h=self.rnn(e); return self.fc(h.squeeze(0))
m=ChatRNN()
print(m(torch.tensor([[0,1]])).shape, " ready — extend with dataset + training loop")
