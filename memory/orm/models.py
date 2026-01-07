from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100, unique=True)
    class Meta:
        table = "users"


class MessageMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.CharField(max_length=100, unique=True)
    conversation_id = fields.CharField(max_length=100)
    class Meta:
        table = "message_memories"


class ChatMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.ForeignKeyField('models.MessageMemory', related_name='MemoryChat')
    message = fields.TextField()
    
    class Meta:
        table = "chat_memories"


class ToolMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.ForeignKeyField('models.MessageMemory', related_name='MemoryTool')
    message = fields.TextField()
    
    class Meta:
        table = "tool_memories"