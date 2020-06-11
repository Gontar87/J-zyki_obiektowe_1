from controllers.controller import Controller
from controllers.app import App


def main():
    controller = Controller()
    app = App(controller)
    app.run_app()


if '__main__' == __name__:
    main()
