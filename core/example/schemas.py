from core.example.models import ToDo
from ext.marshmallow import ma


class ToDoSchema(ma.ModelSchema):
    class Meta:
        model = ToDo
