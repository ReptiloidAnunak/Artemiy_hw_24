from marshmallow import Schema, fields

class UserQuery:
    def __init__(self, query: dict) -> None:
        self.cmd1 = query.get('cmd1')
        self.value1 = query.get('value1')
        self.cmd2 = query.get('cmd2')
        self.value2 = query.get('value2')
        self.file_name = query.get('file_name')

class UserQuerySchema(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)

