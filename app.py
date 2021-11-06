from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask("__main__", template_folder=os.getcwd()+'/templates', static_folder=os.getcwd()+"/static")
app.config["DEBUG"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = rf'sqlite:///{os.getcwd()}/dbdir/test.db'
app.config['secret_key'] = os.getenv("KEY")
app.secret_key = os.getenv("KEY")
db = SQLAlchemy(app)
socketio = SocketIO(app)


@app.route("/")
def handle_home():
    return render_template("draw.html")


if __name__ == "__main__":
    socketio.run(app)
