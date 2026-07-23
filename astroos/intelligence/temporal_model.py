"""Trainable temporal encoder for longitudinal AstroOS feature sequences."""
try:
 import torch
 from torch import nn
except ImportError: torch=None; nn=None

if nn:
 class AstroTemporalModel(nn.Module):
  def __init__(self,input_size,hidden=128,layers=2,num_classes=2):
   super().__init__(); self.rnn=nn.GRU(input_size,hidden,layers,batch_first=True); self.norm=nn.LayerNorm(hidden); self.head=nn.Linear(hidden,num_classes)
  def forward(self,x):
   y,_=self.rnn(x); return self.head(self.norm(y[:,-1]))

def sequence_windows(rows,window,horizon=1):
 return [(rows[i:i+window],rows[i+window:i+window+horizon]) for i in range(max(0,len(rows)-window-horizon+1))]
