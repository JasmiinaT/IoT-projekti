import machine, onewire, ds18x20, time, math
#Thermistori
sensor = machine.ADC(1)
#Digisensorin pinni
ds_pin = machine.Pin(16)
#Digisensori obj
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

#Etsii digi sensorin
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

def ReadAnalogTemp(sensor):
    adcValue = sensor.read_u16()
    voltage = adcValue * 3.3 / 65535
    #print(voltage)
    R_ntc = (voltage * 10000) / (3.3 - voltage)
    # Pinnin impedanssin huomioon otto (30000 - 50000)
    R_PinInImpedanssi = 30000
    R_ntc = 1 / ((1 / R_ntc) - (1 / R_PinInImpedanssi))
    #print(R_ntc)
    #Steinhart kertoimet laskettu datalehden arvoista
    A = 1.137307474E-03
    B = 2.328871275E-04
    C = 0.9181841237E-07
    lnR = math.log(R_ntc)
    temp_kelvin = 1 / (A + (B * lnR) + C * math.pow(lnR, 3))
    return temp_kelvin - 273.15

def ReadDigitalTemp(rom):
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    return ds_sensor.read_temp(rom)

while True:
    DigitaltempC = ReadDigitalTemp(roms[0])
    AnalogTempC = ReadAnalogTemp(sensor)
    print('AnalogLampotila', round(AnalogTempC, 2), 'DigiLampotila', round(DigitaltempC, 2))
    #time.sleep(1)
