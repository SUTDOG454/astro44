import json
from pathlib import Path

from jsonschema import Draft202012Validator


def test_astroschema_v3_is_valid_schema():
    schema = json.loads(Path("schemas/AstroSchema_v3.json").read_text())
    Draft202012Validator.check_schema(schema)
