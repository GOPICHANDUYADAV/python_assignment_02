#smart home device control
class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.device_id} turned on")

    def turn_off(self):
        self.status = "off"
        print(f"{self.device_id} turned off")


class SmartLight(SmartDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def turn_on(self):
        self.status = "on"
        self.brightness = 100
        print(f"SmartLight {self.device_id} turned on. Brightness set to 100%")


class SmartThermostat(SmartDevice):
    def __init__(self, device_id, temperature=22):
        super().__init__(device_id)
        self.temperature = temperature

    def turn_on(self):
        self.status = "on"
        print(f"SmartThermostat {self.device_id} turned on. Temperature set to {self.temperature}°C")


class SmartHomeHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_all_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()


# Test
hub = SmartHomeHub()

hub.add_device(SmartLight("L01"))
hub.add_device(SmartThermostat("T01"))

hub.turn_all_on()
hub.turn_all_off()