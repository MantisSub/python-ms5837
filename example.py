#!/usr/bin/python
from time import sleep
from ms5837 import MS5837_30BA, UNITS_atm, UNITS_Torr, UNITS_psi, UNITS_Centigrade, UNITS_Farenheit, UNITS_Kelvin, DENSITY_SALTWATER

sensor = MS5837_30BA()  # Default I2C bus is 1 (Raspberry Pi 3)
# sensor = MS5837_30BA(0) # Specify I2C bus
# sensor = MS5837_02BA()
# sensor = MS5837_02BA(0)
# sensor = ms5837(model=MS5837_MODEL_30BA, bus=0) # Specify model and bus

# We must initialize the sensor before reading it
if not sensor.init():
    print("Sensor could not be initialized")
    exit(1)

# We have to read values from sensor to update pressure and temperature
if not sensor.read():
    print("Sensor read failed!")
    exit(1)

print("Pressure: %.2f atm  %.2f Torr  %.2f psi") % (
    sensor.pressure(UNITS_atm),
    sensor.pressure(UNITS_Torr),
    sensor.pressure(UNITS_psi))

print("Temperature: %.2f C  %.2f F  %.2f K") % (
    sensor.temperature(UNITS_Centigrade),
    sensor.temperature(UNITS_Farenheit),
    sensor.temperature(UNITS_Kelvin))

freshwaterDepth = sensor.depth()  # default is freshwater
sensor.setFluidDensity(DENSITY_SALTWATER)
saltwaterDepth = sensor.depth()  # No nead to read() again
sensor.setFluidDensity(1000)  # kg/m^3
print("Depth: %.3f m (freshwater)  %.3f m (saltwater)") % (freshwaterDepth, saltwaterDepth)

# fluidDensity doesn't matter for altitude() (always MSL air density)
print("MSL Relative Altitude: %.2f m") % sensor.altitude()  # relative to Mean Sea Level pressure in air

sleep(5)

# Spew readings
while True:
    if sensor.read():
        print("P: %0.1f mbar  %0.3f psi\tT: %0.2f C  %0.2f F") % (
            sensor.pressure(),  # Default is mbar (no arguments)
            sensor.pressure(UNITS_psi),  # Request psi
            sensor.temperature(),  # Default is degrees C (no arguments)
            sensor.temperature(UNITS_Farenheit))  # Request Farenheit
        sleep(2)
    else:
        print("Sensor read failed!")
        exit(1)
