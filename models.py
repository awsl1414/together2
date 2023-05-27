from tortoise.models import Model
from tortoise import fields


class Info(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, null=False, descrrption="姓名")
    tel = fields.CharField(max_length=64, null=False, description="电话")
