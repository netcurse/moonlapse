from app.server.core import Core

PORT = 42523

if __name__ == '__main__':
    core = Core(PORT)
    core.run()
