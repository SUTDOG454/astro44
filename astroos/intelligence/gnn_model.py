"""Trainable AFM graph model with optional PyTorch Geometric backend."""
try:
 import torch
 from torch import nn
 from torch_geometric.nn import GCNConv
except ImportError: torch=None; nn=None; GCNConv=None

if nn:
 class AstroGNN(nn.Module):
  def __init__(self,in_channels,hidden=128,out_channels=64,num_classes=2):
   super().__init__(); self.g1=GCNConv(in_channels,hidden); self.g2=GCNConv(hidden,out_channels); self.head=nn.Linear(out_channels,num_classes)
  def forward(self,x,edge_index,batch=None):
   x=self.g1(x,edge_index).relu(); x=self.g2(x,edge_index).relu()
   if batch is None: pooled=x.mean(dim=0,keepdim=True)
   else:
    from torch_geometric.nn import global_mean_pool; pooled=global_mean_pool(x,batch)
   return self.head(pooled)

def train_epoch(model,optimizer,criterion,batch):
 if torch is None: raise RuntimeError('torch is required')
 model.train(); optimizer.zero_grad(); logits=model(batch.x,batch.edge_index,getattr(batch,'batch',None)); loss=criterion(logits,batch.y); loss.backward(); optimizer.step(); return float(loss.detach().cpu())
