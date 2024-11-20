from tortoise.fields import IntField, CharField, DateField
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator



class Student(Model):
    id = IntField(pk=True)
    name = CharField(max_length=50)
    birth_date = DateField()

    class Meta:
        table = "students"



Student_Pydantic= pydantic_model_creator(Student)
