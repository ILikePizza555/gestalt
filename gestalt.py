from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OEYWKSP EHEOEVROEBDLD '
socketio = SocketIO(app)

@app.route('/')
def app_view():
	

if __name__ == '__main__':
	socketio.run(app)
