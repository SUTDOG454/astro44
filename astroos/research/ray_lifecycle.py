"""Reproducible Ray experiment lifecycle with checkpoint and artifact manifests."""
from dataclasses import dataclass,asdict
from pathlib import Path
import json,hashlib,datetime
@dataclass
class RunManifest:
    run_id:str; hypothesis_id:str; seed:int; config:dict; dataset_hash:str; status:str='created'; checkpoint_uri:str=''; artifact_uri:str=''

def write_manifest(manifest,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(asdict(manifest),indent=2,sort_keys=True)); return str(p)

def hash_dataset(data): return hashlib.sha256(json.dumps(data,sort_keys=True,default=str).encode()).hexdigest()

def checkpoint_payload(model_state,metrics,epoch): return {'epoch':epoch,'metrics':metrics,'model_state':model_state,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}

def resource_plan(num_workers=1,cpu_per_worker=1,gpu_per_worker=0): return {'num_workers':num_workers,'resources':{'CPU':cpu_per_worker,'GPU':gpu_per_worker}}
