from sanic import Sanic, response

app = Sanic()

@app.route('/')
def app_view():
	return response.file("chat.html")

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=9000)