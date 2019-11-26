import smbus2
import bme280
from datetime import datetime
def truncate(n):
        return int(n * 10000) / 10000

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
I = "        "
data = bme280.sample(bus, address, calibration_params)
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(I), truncate(data.temperature),(I), truncate(data.pressure), file=open("output.txt", "a+"))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(truncate(data.temperature))
print(truncate(data.pressure))
print(truncate(data.humidity))

