#! /usr/bin/python3

from bleach import Cleaner
from bleach.linkifier import LinkifyFilter
from sanic import Sanic, response
import socketio

STATIC_ASSETS_PATH = "./static"
LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 9000

inputCleaner = Cleaner(filters=[LinkifyFilter])

sio = socketio.AsyncServer(async_mode='sanic')
app = Sanic(name="gestalt")
sio.attach(app)
app.static("/static", STATIC_ASSETS_PATH)

@app.route('/')
async def app_view(request):
	return response.file("chat.html")

@sio.event()
async def message(sid, data):
	print("Sid: ", sid, " Data: ", data)

	sanitizedText = inputCleaner.clean(data.text)
	sio.emit("message", {"author": "The Hive", "color": "yellow", "text": sanitizedText})

if __name__ == "__main__":
	app.run(host=LISTEN_HOST, port=LISTEN_PORT)