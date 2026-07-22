"""Feature-store abstraction with deterministic record identity."""
import hashlib,json

def feature_id(entity_id,timestamp,features):
    payload=json.dumps({'entity_id':entity_id,'timestamp':timestamp,'features':features},sort_keys=True,separators=(',',':'))
    return hashlib.sha256(payload.encode()).hexdigest()

class FeatureStore:
    def __init__(self,backend): self.backend=backend
    def put(self,entity_id,timestamp,features,provenance=None):
        record={'feature_id':feature_id(entity_id,timestamp,features),'entity_id':entity_id,'timestamp':timestamp,'features':features,'provenance':provenance or {}}
        self.backend.write(record); return record['feature_id']
    def get(self,feature_id_value): return self.backend.read(feature_id_value)
