import asyncio
import websockets
import os
import time

async def check_and_send_images(websocket, path, last_mod_times):
    while True:
        try:
            for image_name, last_mod_time in list(last_mod_times.items()):
                image_path = image_name
                if os.path.exists(image_path):
                    new_mod_time = os.path.getmtime(image_path)
                    if new_mod_time > last_mod_time:
                        # Update the last modification time
                        last_mod_times[image_name] = new_mod_time
                        # Send the file
                        await websocket.send(os.path.basename(image_path))
                        with open(image_path, "rb") as image:
                            await websocket.send(image.read())
                            print(f"Image {os.path.basename(image_path)} sent")
                else:
                    await websocket.send(f"{image_name} not found")
                    print(f"{image_name} not found")
            await asyncio.sleep(5)  # Check every 5 seconds
        except websockets.exceptions.ConnectionClosed:
            print("Connection Closed")
            break

async def handler(websocket, path):
    image_files = ['Before Cholecap_cholesterol_plot.png', 'After Cholecap_cholesterol_plot.png', 'Before Competitor A_cholesterol_plot.png', 'After Competitor A_cholesterol_plot.png', 'Before Competitor B_cholesterol_plot.png', 'After Competitor B_cholesterol_plot.png']
    last_mod_times = {}

    for image_file in image_files:
        if os.path.exists(image_file):
            last_mod_times[image_file] = os.path.getmtime(image_file)
            await websocket.send(os.path.basename(image_file))
            with open(image_file, "rb") as image:
                await websocket.send(image.read())
                print(f"Initial image {os.path.basename(image_file)} sent")
            await asyncio.sleep(2)
        else:
            await websocket.send(f"{image_file} not found")
            print(f"{image_file} not found")

    await check_and_send_images(websocket, path, last_mod_times)

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("Server started")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
