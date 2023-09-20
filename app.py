import asyncio
import websockets
import logging

LOCAL_URL: str = "0.0.0.0"
LOCAL_PORT: int = 10000

async def echo(websocket, path):
    async for message in websocket:
        # Echo back the received message to the client
        logging.warning("Received message: " + message) # Please work
        print("Received message: " + message)
        await websocket.send(message)

def main():
    print("Starting server...")
    start_server = websockets.serve(echo, LOCAL_URL, LOCAL_PORT)
    
    # Create and run an asyncio event loop
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(start_server)

    try:
        print("Server started at wss://" + LOCAL_URL + ":" + str(LOCAL_PORT))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())

if __name__ == "__main__":
    print('Entering main...')
    main()