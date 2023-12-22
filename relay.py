import machine
import time

# 设置继电器所连接的GPIO引脚
relay_pin = machine.Pin(17, machine.Pin.OUT)  # 根据实际连接选择引脚

# 控制继电器打开
relay_pin.value(1)
time.sleep(2)  # 等待2秒

# 控制继电器关闭
relay_pin.value(0)


class Relay:
    def __init__(self, gpio):
        self.pin = machine.Pin(gpio, machine.Pin.OUT)

    def on(self):
        return self.pin.on()

    def off(self):
        return self.pin.off()

    def open_once(self, ts=2000):
        """
        :param ts: milliseconds since the epoch
        :return:
        """
        self.on()
        time.sleep(ts / 1000)
        self.off()
