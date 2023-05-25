from flask_script import Manager, Server

from apps import create_app

app = create_app()

server = Server(host='127.0.0.1', port=5001)

manager = Manager(app=app)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()