"""AFM/AFA dataset construction, normalization, and model training interfaces."""
import math

from astroos.analytics import posthog_client

def flatten_feature_tensor(record):
    vals=[]
    def walk(x):
        if isinstance(x,(int,float)) and math.isfinite(float(x)): vals.append(float(x))
        elif isinstance(x,dict):
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(record); return vals

class StandardScaler:
    def fit(self,rows):
        n=max(len(rows),1); width=max((len(r) for r in rows),default=0); self.mean=[sum((r[i] if i<len(r) else 0) for r in rows)/n for i in range(width)]; self.std=[]
        for i,m in enumerate(self.mean): self.std.append(max((sum(((r[i] if i<len(r) else 0)-m)**2 for r in rows)/n)**0.5,1e-8))
        return self
    def transform(self,rows): return [[((r[i] if i<len(r) else 0)-self.mean[i])/self.std[i] for i in range(len(self.mean))] for r in rows]

def build_supervised_dataset(records,label_key):
    X=[]; y=[]
    for r in records:X.append(flatten_feature_tensor(r['features'])); y.append(r['labels'][label_key])
    scaler=StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    if posthog_client is not None:
        posthog_client.capture(
            "training_dataset_built",
            distinct_id="$astroos_system",
            properties={
                "sample_count": len(X),
                "feature_width": len(scaler.mean) if scaler.mean else 0,
                "label_key": label_key,
                "$process_person_profile": False,
            },
        )
    return X_scaled,y,scaler

def chronological_split(X,y,train_fraction=.7,val_fraction=.15):
    n=len(X); a=int(n*train_fraction); b=int(n*(train_fraction+val_fraction)); return (X[:a],y[:a]),(X[a:b],y[a:b]),(X[b:],y[b:])
