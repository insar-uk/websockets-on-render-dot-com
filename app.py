import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        # Echo back the received message to the client
        print("Received message: " + message)
        await websocket.send(message)

if __name__ == "__main__":

    print("Starting server...")
    
    start_server = websockets.serve(echo, "localhost", 8080)

    # Create and run an asyncio event loop
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(start_server)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
