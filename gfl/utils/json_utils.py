import json


class JsonType(object):

    def __init__(self, type_tuple):
        super(JsonType, self).__init__()

    def instance(self):
        pass


class JsonUtils(object):

    @classmethod
    def to_dict(cls, obj):
        pass

    @classmethod
    def from_dict(cls, dt, obj_type):
        pass

    @classmethod
    def to_json(cls, obj, pretty=True):
        dt = cls.to_dict(obj)
        if pretty:
            return json.dumps(dt, indent=4)
        else:
            return json.dumps(dt)

    @classmethod
    def from_json(cls, json_str, obj_type):
        dt = json.loads(json_str)
        return cls.from_dict(dt, obj_type)
        pass