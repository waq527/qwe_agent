from typing import AsyncGenerator
from openai import AsyncOpenAI
import config

class Agentbase:
    def __init__(self, url: str, key: str):
        self.client = AsyncOpenAI(base_url=url, api_key=key)

    async def send_messages(self, messages) -> AsyncGenerator[str, None]:
        response_stream = await self.client.chat.completions.create(
            model=config.LLMMODEL,
            messages=messages,
            stream=True,
        )
        async for chunk in response_stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    




if __name__ == "__main__":
    agent = Agentbase(config.LLMURL, config.LLMKEY)
    import asyncio
    async def test_stream():
        """正确使用流式响应"""
        agent = Agentbase(config.LLMURL, config.LLMKEY)
        # async for 异步迭代器
        async for chunk in agent.send_messages([
            {"role": "system", "content": ""},
            {"role": "user", "content": ""},
            {"role": "assistant", "content": ""},
            {"role": "user", "content": "continue."},
        ]):
            print(chunk, end="", flush=True)  # 实时打印每个块
    asyncio.run(test_stream())
    
    