import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)
print((data.timestamp),":Datums", file=open("output.txt", "a+"))
print((data.temperature),":temperatura", file=open("output.txt", "a+"))
print((data.pressure),":spiediens", file=open("output.txt", "a+"))
print((data.humidity),"mitrums", file=open("output.txt", "a+"))
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

