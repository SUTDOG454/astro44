"""Optional PyTorch Geometric adapter for AstroOS graph features."""
try:
    import torch
    from torch import nn
    from torch_geometric.nn import GCNConv
except ImportError:
    torch=None; nn=None; GCNConv=None

if nn:
    class AstroGraphEncoder(nn.Module):
        def __init__(self,in_channels,hidden_channels=64,out_channels=64):
            super().__init__(); self.conv1=GCNConv(in_channels,hidden_channels); self.conv2=GCNConv(hidden_channels,out_channels)
        def forward(self,x,edge_index):
            x=self.conv1(x,edge_index).relu(); return self.conv2(x,edge_index)
else:
    class AstroGraphEncoder:
        def __init__(self,*args,**kwargs): raise RuntimeError("torch and torch-geometric are required")
