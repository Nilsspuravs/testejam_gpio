import smbus2
import bme280
from datetime import datetime
def truncate(n):
        return int(n * 1000) / 1000

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
I = " "
data = bme280.sample(bus, address, calibration_params)
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(I), truncate(data.temperature, 2),(I), truncate(data.pressure, 2), file=open("output.txt", "a+"))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(data.temperature)
print(data.pressure)
print(data.humidity)

