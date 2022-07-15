
import asyncio
import json
import websockets


def 


async def main(uri):
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "type": "subscribe",
            "feeds": [
                "orderbook.sfox.ethbtc",
            ],
        }))
        async for msg in ws:
            print(msg)
asyncio.run(main("wss://ws.sfox.com/ws"))