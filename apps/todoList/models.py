from pydantic.v1.validators import max_str_int
from tortoise.fields import IntField, CharField
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

import datetime
from tortoise import fields

class DatetimeField(fields.DatetimeField):
    """重载日期时间模型字段"""

    def __init__(self, *args, **kwargs):
        super(DatetimeField, self).__init__(*args, **kwargs)

    def to_python_value(self, value: datetime.datetime) -> [str, None]:
        if value is None:
            value = None
        else:
            try:
                value = value.strftime("%Y-%m-%d")
                self.validate(value)
            except Exception as ex:
                value = super(DatetimeField, self).to_python_value(value)
        return value

fields.DatetimeField = DatetimeField


class TodoList(Model):
    id = IntField(pk=True)
    content = CharField(max_length=50)
    before_time = DatetimeField()
    is_delete = IntField(max_str_int=10)
    create_time = DatetimeField()
    update_time = DatetimeField()
    done_time = DatetimeField()

    class Meta:
        table = "todoList"


todoListPydantic = pydantic_model_creator(TodoList)
