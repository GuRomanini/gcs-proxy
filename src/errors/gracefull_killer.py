import signal


class GracefulKillerException(Exception):
    def __init__(self) -> None:
        super().__init__()


class GracefulKiller:
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        raise GracefulKillerException()
