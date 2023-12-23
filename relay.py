import time

from gpiozero import OutputDevice


class Relay:
    def __init__(self, gpio):
        self.device = OutputDevice(gpio, active_high=True, initial_value=False)

    def on(self):
        return self.device.on()

    def off(self):
        return self.device.off()

    def open_once(self, ts=1000):
        """
        :param ts: milliseconds since the epoch
        :return:
        """
        self.on()
        time.sleep(ts / 1000)
        self.off()
