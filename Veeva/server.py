import asyncio
import websockets
import os

async def send_image(websocket, path):
    image_path = 'b.png'  # Update this with the path to your PNG file
    if os.path.exists(image_path):
        await websocket.send(os.path.basename(image_path))  # Send the filename first
        with open(image_path, "rb") as image:
            await websocket.send(image.read())
            print("Image and filename sent")
    else:
        await websocket.send("File not found")
        print("File not found")

async def main():
    async with websockets.serve(send_image, "localhost", 6789):
        print("Server started")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
