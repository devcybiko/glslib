import json
from datetime import datetime, date

from munch import DefaultMunch

class GJSON:
    @classmethod
    def _json_deserializer(cls, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return str(obj)
        # raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    @classmethod
    def load(cls, file_path):
        import json5
        with open(file_path, 'r') as f:
            return json5.load(f)
    
    @classmethod
    def dumps(cls, obj, indent=2,sort_keys=False):
        return json.dumps(obj, sort_keys=sort_keys, default=cls._json_deserializer, indent=indent if isinstance(obj, (dict, list)) else None)

    @classmethod
    def dump(cls, obj, file_path, indent=2, sort_keys=False):
        with open(file_path, 'w') as f:
            json.dump(obj, f, sort_keys=sort_keys, default=cls._json_deserializer, indent=indent if isinstance(obj, (dict, list)) else None)

    @classmethod
    def loads(cls, json_str):
        import json5
        return json5.loads(json_str)

    @classmethod
    def print(cls, obj, indent=2, sort_keys=False):
        print(cls.dumps(obj, indent=indent, sort_keys=sort_keys))

    @classmethod
    def sort(cls, d: dict) -> dict:
        """Recursively sort a dict by keys."""
        if isinstance(d, DefaultMunch):
            return DefaultMunch(**{k: cls.sort(d[k]) for k in sorted(d.keys())})
        elif isinstance(d, dict):
            return {k: cls.sort(d[k]) for k in sorted(d.keys())}
        elif isinstance(d, list):
            return [cls.sort(item) for item in d]
        else:
            return d
