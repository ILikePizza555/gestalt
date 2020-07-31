#! /usr/bin/python3

from bleach import Cleaner
from bleach.linkifier import LinkifyFilter
from sanic import Sanic, response
import socketio
import os

STATIC_ASSETS_PATH = "./static"
LISTEN_HOST = os.getenv("GESTALT_LISTEN_HOST", default="0.0.0.0")
LISTEN_PORT = os.getenv("GESTALT_LISTEN_PORT", default=80)

inputCleaner = Cleaner(filters=[LinkifyFilter])

app = Sanic(name="gestalt")
app.static("/static", STATIC_ASSETS_PATH)

@app.route('/')
async def app_view(request):
	return await response.file("chat.html")

sio = socketio.AsyncServer(async_mode='sanic')
sio.attach(app)

@sio.event()
async def message(sid: str, data: dict):
	sanitizedText = inputCleaner.clean(data["text"])
	await sio.emit("message", {"author": "The Hive", "color": "#f1c40f", "text": sanitizedText})

if __name__ == "__main__":
	app.run(host=LISTEN_HOST, port=LISTEN_PORT)