"""Distributed Ray training orchestration with checkpoint persistence."""
from pathlib import Path
import json
try: import ray
except ImportError: ray=None

def save_checkpoint(state,path):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(state,default=str,sort_keys=True)); return str(p)

def run_trials(configs,train_fn,resources=None):
 if ray is None:return [train_fn(c) for c in configs]
 remote=ray.remote(train_fn)
 if resources:
  remote=remote.options(num_cpus=resources.get('CPU',1),num_gpus=resources.get('GPU',0))
 return ray.get([remote.remote(c) for c in configs])
