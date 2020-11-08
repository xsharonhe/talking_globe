from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room
from PIL import ImageFont, ImageDraw, Image

app = Flask(__name__)
socketio = SocketIO(app)

def string_to_image(filename = "message.png", text="hello", size = 300, txtcolor = "white", height = 2):
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf", size) ## FONT CHANGE WINDOWS VS OS
    # creates the image
    # size is modified depending on length of the string (length, height)
    image = Image.new(mode = "RGB", size = (int(size/2)*len(text), size+height), color = "black") 
    draw = ImageDraw.Draw(image)
    
    width, height = image.size
    resized_img = image.resize((int(((70*width)/height)), 70), Image.BILINEAR)
    
    # draws out the text
    draw.text((10,10), text, font=font, fill = txtcolor, align = "center")
    image.show()
    #saves the image file
    image.save(filename)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat_room():
    username = request.args.get("username")
    room = request.args.get("room")

    if username and room:
        return render_template("chat.html", username=username, room=room)
    else:
        return redirect(url_for("home"))

@socketio.on("send_message")
def handle_send_message_event(data):
    string_to_image(filename = 'todelete.bmp', text = data["message"], size = 100, txtcolor = "white", height = 50)
    socketio.emit("receive_message", data, room=data['room'])

@socketio.on("join_room")
def handle_join_room(data):
    join_room(data['room'])
    socketio.emit("join_room_announcement", data, room=data['room'])

@socketio.on("leave_room")
def handle_leave_room(data):
    leave_room(data["room"])
    socketio.emit("leave_room_announcement", data, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)