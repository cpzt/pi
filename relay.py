import time

from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory


class Relay:
    """Remote control relay, including Docker"""

    def __init__(self, host, gpio):
        # Initialize the PiGPIOFactory with the specified host.
        factory = PiGPIOFactory(host=host)

        # When the relay is open (current disconnected), the GPIO output signal is low,
        # the initial value is 0, and the target value is 0.
        # When the relay is closed (current connected), the GPIO output signal is high.
        self.device = DigitalOutputDevice(gpio,
                                          active_high=False,
                                          initial_value=False,
                                          pin_factory=factory)

    def on(self):
        """Close the relay circuit (current flows)"""
        return self.device.on()

    def off(self):
        """Open the relay circuit (current disconnected)"""
        return self.device.off()

    def open_once(self, ts=200):
        """
        :param ts: milliseconds since the epoch
        :return:
        """
        try:
            # Close the circuit
            self.on()
            time.sleep(ts / 1000)
            self.off()
        except Exception:  # noqa
            pass
        finally:
            # Ensure the relay is open when the function ends
            self.off()

    def test(self):
        try:
            while True:
                # Close the circuit
                self.device.on()
                print("Relay closed, output signal status:", self.device.value)
                time.sleep(2)  # Wait for 5 seconds

                # Open the circuit
                self.device.off()
                print("Relay open, output signal status:", self.device.value)
                time.sleep(2)  # Wait for 5 seconds

        except KeyboardInterrupt:
            print("Program interrupted by the user")
        finally:
            # Ensure the relay is open when the program ends
            self.device.off()


if __name__ == "__main__":
    relay = Relay("hostname", 17)
    relay.test()
