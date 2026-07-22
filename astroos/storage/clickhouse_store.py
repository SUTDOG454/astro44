"""ClickHouse feature store and schema migration runner."""
import json
class ClickHouseFeatureStore:
    def __init__(self,client,table='astroos.chart_features'): self.client=client; self.table=table
    def write(self,record):
        self.client.insert(self.table,[[record['entity_id'],record['timestamp'],record.get('schema_version','1.0'),json.dumps(record['features'],sort_keys=True),json.dumps(record.get('provenance',{}),sort_keys=True)]],column_names=['chart_id','event_time','schema_version','feature_json','provenance_json'])
    def read(self,feature_id): return self.client.query('SELECT * FROM '+self.table+' WHERE chart_id=%(id)s ORDER BY event_time DESC LIMIT 1',parameters={'id':feature_id}).result_rows

MIGRATIONS={1:'CREATE DATABASE IF NOT EXISTS astroos',2:'ALTER TABLE astroos.chart_features ADD COLUMN IF NOT EXISTS schema_version LowCardinality(String) DEFAULT \'1.0\''}
def migrate(client,current,target):
    for version in range(current+1,target+1): client.command(MIGRATIONS[version])
