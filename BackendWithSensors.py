import network
import time
import machine
import requests
import onewire
import ds18x20
import math

#Sensor setup
#Thermistor pin
sensor = machine.ADC(1)
#Digisensorin pinni
ds_pin = machine.Pin(16)
#Digisensori obj
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

#Etsii digi sensorin
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

# Replace "?" with your own credentials
ssid = '??????'
password = '??????'
apikey = "T9S32VCI1I6CH7HY"

def Wificon(ssid, pswd):
    # Initialize the Wi-Fi interface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the Wi-Fi network
    wlan.connect(ssid, pswd)

    # Check the connection status
    if wlan.status() != 3:
        raise RuntimeError('Connection failed')
    else:
        print('Connected')
        ip = wlan.ifconfig()
        print('IP address:', ip)
    return None

def Read_temp(sensor):
    # Read temperature sensor
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
    temperature = round((temp_kelvin - 273.15), 2)
    return temperature

def Read_ref(rom):
    # Read reference temperature
    ds_sensor.convert_temp()
    time.sleep_ms(750) # Gives sensor time to convert
    ref_temp = round(ds_sensor.read_temp(rom), 2)
    return ref_temp

def Send_temp(temp, ref, api):
    # Send temperature to Thingspeak
    thingspeak_http = f'https://api.thingspeak.com/update?api_key={api}&field1={temp}&field2={ref}'
    response = requests.get(thingspeak_http)
    response.close()
    print(temp)
    print(ref)
    return None

def Main(api):
    Wificon(ssid, password)
    while True:
        temperature = Read_temp(sensor)
        ref_temp = Read_ref(roms[0])
        Send_temp(temperature, ref_temp, api)
        time.sleep(10)  # Set interval for measurement (s)

Main(apikey)