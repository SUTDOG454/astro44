"""Model registry abstraction with immutable artifact metadata."""
from dataclasses import dataclass,asdict
from datetime import datetime,timezone
import hashlib,json
@dataclass(frozen=True)
class ModelArtifact:
    model_id:str; version:str; model_type:str; artifact_uri:str; metrics:dict; dataset_hash:str; created_at:str

def dataset_hash(dataset): return hashlib.sha256(json.dumps(dataset,sort_keys=True,default=str).encode()).hexdigest()
class ModelRegistry:
    def __init__(self,backend): self.backend=backend
    def register(self,model_id,version,model_type,artifact_uri,metrics,dataset):
        a=ModelArtifact(model_id,version,model_type,artifact_uri,metrics,dataset_hash(dataset),datetime.now(timezone.utc).isoformat()); self.backend.put(asdict(a)); return a
    def get(self,model_id,version): return self.backend.get(model_id,version)
