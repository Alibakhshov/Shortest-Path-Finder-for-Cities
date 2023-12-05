from flask_app import create_app, socketio

app, _, _ = create_app()

if __name__ == "__main__":
    socketio.run(app)
