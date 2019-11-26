import smbus2
import bme280
from datetime import datetime

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(I), (data.temperature),(I), (data.pressure), file=open("output.txt", "a+"))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(data.temperature)
print(data.pressure)
print(data.humidity)

