import asyncio
import websockets
import os
import time

async def check_and_send_image(websocket, path, last_mod_time):
    images = [f"{i}.png" for i in range(1, 22)]
    image_path = 'a.png'
    while True:
        try:
            # Check if the file exists and get its last modification time
            if os.path.exists(image_path):
                new_mod_time = os.path.getmtime(image_path)
                if new_mod_time > last_mod_time:
                    # Update the last modification time
                    last_mod_time = new_mod_time
                    # Send the file
                    await websocket.send(os.path.basename(image_path))
                    with open(image_path, "rb") as image:
                        await websocket.send(image.read())
                        print(f"Image {os.path.basename(image_path)} sent")
            else:
                await websocket.send("File not found")
                print("File not found")
            await asyncio.sleep(5)  # Check every 5 seconds
        except websockets.exceptions.ConnectionClosed:
            print("Connection Closed")
            break

async def handler(websocket, path):
    image_path = 'a.png'
    if os.path.exists(image_path):
        last_mod_time = os.path.getmtime(image_path)
        # Send the initial image
        await websocket.send(os.path.basename(image_path))
        with open(image_path, "rb") as image:
            await websocket.send(image.read())
            print(f"Initial image {os.path.basename(image_path)} sent")
        await check_and_send_image(websocket, path, last_mod_time)
    else:
        await websocket.send("File not found")
        print("File not found")

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("Server started")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
