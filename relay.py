import machine
import time


class Relay:
    def __init__(self, gpio):
        self.pin = machine.Pin(gpio, machine.Pin.OUT)

    def on(self):
        return self.pin.on()

    def off(self):
        return self.pin.off()

    def open_once(self, ts=1000):
        """
        :param ts: milliseconds since the epoch
        :return:
        """
        self.on()
        time.sleep(ts / 1000)
        self.off()
