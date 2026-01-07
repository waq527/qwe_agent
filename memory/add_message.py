from tortoise import Tortoise, run_async
from memory.orm.models import MessageMemory, ChatMemory, ToolMemory
from tortoise.transactions import in_transaction

async def create_memories_with_message(conversation_id: str, message_id: str, chat_message: str, tool_message: str):
    try:
        # 使用事务确保数据一致性
        async with in_transaction():
            # 1. 首先创建 MessageMemory
            message_memory = await MessageMemory.create(
                message_id=message_id,
                conversation_id=conversation_id
            )
            
            # 2. 创建关联的 ChatMemory
            await ChatMemory.create(
                message_id=message_memory,  # 这里传递 MessageMemory 实例
                chat_message=chat_message
            )
            
            # 3. 创建关联的 ToolMemory
            await ToolMemory.create(
                message_id=message_memory,  # 这里传递 MessageMemory 实例
                tool_message=tool_message
            )
            
    except Exception as e:
        print(f"创建失败: {e}")
        raise