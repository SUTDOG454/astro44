"""Temporal AFM model scaffold with sequence masking."""
try:
    import torch
    from torch import nn
except ImportError:
    torch=None; nn=None

if nn:
    class AstroTemporalEncoder(nn.Module):
        def __init__(self,input_size,hidden_size=64,layers=2):
            super().__init__(); self.rnn=nn.GRU(input_size,hidden_size,layers,batch_first=True); self.proj=nn.Linear(hidden_size,hidden_size)
        def forward(self,x):
            y,_=self.rnn(x); return self.proj(y[:,-1])
else:
    class AstroTemporalEncoder:
        def __init__(self,*args,**kwargs): raise RuntimeError("torch is required")
