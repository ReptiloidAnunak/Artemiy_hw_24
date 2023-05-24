from dataclasses import dataclass
import marshmallow_dataclass
from typing import Optional

@dataclass
class UserQuery:
    cmd1: str
    value1: str
    cmd2: str
    value2: str
    file_name: str


UserQuerySchema = marshmallow_dataclass.class_schema(UserQuery)
