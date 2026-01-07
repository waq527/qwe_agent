from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"


class MessageMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.CharField(max_length=100, unique=True)
    conversation_id = fields.CharField(max_length=100)

    class Meta:
        table = "message_memories"
        ordering = ["id"]


class ChatMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.ForeignKeyField('models.MessageMemory', related_name='MemoryChat')
    chat_message = fields.TextField()

    class Meta:
        table = "chat_memories"
        ordering = ["id"]


class ToolMemory(Model):
    id = fields.IntField(pk=True)
    message_id = fields.ForeignKeyField('models.MessageMemory', related_name='MemoryTool')
    tool_message = fields.TextField()
    
    class Meta:
        table = "tool_memories"
        ordering = ["id"]