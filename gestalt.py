#! /usr/bin/python3

from sanic import Sanic, response
import socketio

STATIC_ASSETS_PATH = "./static"
LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 9000

sio = socketio.AsyncServer(async_mode='sanic')
app = Sanic(name="gestalt")
sio.attach(app)
app.static("/static", STATIC_ASSETS_PATH)

@app.route('/')
def app_view(request):
	return response.file("chat.html")

if __name__ == "__main__":
	app.run(host=LISTEN_HOST, port=LISTEN_PORT)