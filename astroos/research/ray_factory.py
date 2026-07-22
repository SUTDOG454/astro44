"""Ray research orchestration with local fallback and experiment metadata."""
from dataclasses import dataclass,asdict
from datetime import datetime,timezone
import uuid
try: import ray
except ImportError: ray=None

@dataclass(frozen=True)
class Experiment:
    experiment_id:str; hypothesis_id:str; created_at:str; seed:int; config:dict

def make_experiment(hypothesis_id,config,seed=42): return Experiment(str(uuid.uuid4()),hypothesis_id,datetime.now(timezone.utc).isoformat(),seed,config)

def run_experiments(experiments,runner):
    if ray is None:return [runner(asdict(e)) for e in experiments]
    remote=ray.remote(runner); return ray.get([remote.remote(asdict(e)) for e in experiments])
