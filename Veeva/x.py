import json
import asyncio
def generate_message (file_path):
    x=0
    return x

async def send_telemetry(websocket):
    device_enum_message = generate_message("device_enum.png")

    await websocket.send(json.dumps(device_enum_message))


    while True:
        await websocket.send(json.dumps(telemetry_message1))
        await asyncio.sleep(1)

async def listen_for_version_request(websocket):
    while True:
        message = await websocket.recv()
        try:
            decoded_message = json.loads(message)
        except json.JSONDecodeError:
            continue

        if decoded_message.get("VERSION_REQUEST") is not None:
            version_reply = {
                "VERSION_REPLY": [
                    {"CSCI": "EXCOMS Service", "VER": "2.1.0"},
                    {"CSCI": "EXCOMS 01", "VER": "2.0.1"},
                    {"CSCI": "EXCOMS 02", "VER": "2.0.1"},
                    {"CSCI": "BT-EXCOMS", "VER": "3.0.0"}
                ]
            }
            await websocket.send(json.dumps(version_reply))

async def send_json(websocket, path):
    # Run both coroutines concurrently
    await asyncio.gather(send_telemetry(websocket), listen_for_version_request(websocket))

# ... (rest of your code for starting the server)








async def send_image(websocket):
    while True:
        with open("image.png", "rb") as image_file:
            image_data = image_file.read()
            await websocket.send(image_data)
        await asyncio.sleep(60)  # Sending the image every second, for example