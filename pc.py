from relay import Relay


class PCController:
    def __init__(self, gpio=18, host=None, password=None):

        self.relay = Relay(gpio)

    def power_on(self):
        self.relay.open_once(ts=1000)

    def power_off(self):
        ...

    def power_off_force(self):
        self.relay.open_once(ts=3000)
