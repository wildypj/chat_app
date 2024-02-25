

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store user information in a dictionary {sid: username}
users = {}

@socketio.on("message")
def handle_message(data):
    username = data.get('username', 'Guest')
    message = data['message']
    recipient = data.get('recipient')

    if recipient and recipient in users.values():  
        recipient_sid = next((sid for sid, name in users.items() if name == recipient), None)
        if recipient_sid:  
            emit("message", {"username": username, "message": message, "recipient": recipient}, room=recipient_sid)
    else:
        send({"username": username, "message": message}, broadcast=True)  

@socketio.on("connect")
def handle_connect():
    username = request.args.get('username', 'Guest')
    users[request.sid] = username
    emit("userList", {"users": list(users.values())}, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    username = users.pop(request.sid, None)
    if username:
        emit("userList", {"users": list(users.values())}, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
