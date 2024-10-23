import network
import time
import machine
import requests

# Replace "?" with your own credentials
SSID = '??????'
PASSWORD = '??????'
APIKEY = "??????"
SENSOR = machine.ADC(4) # Initializes the ADC on pin 4 (Analog-to-Digital Converter)

def Wificon():
    # Initialize the Wi-Fi interface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the Wi-Fi network
    wlan.connect(SSID, PASSWORD)

    # Check the connection status
    if wlan.status() != 3:
        raise RuntimeError('Connection failed')
    else:
        print('Connected')
        ip = wlan.ifconfig()
        print('IP address:', ip)
    return None

def Read_temp():
    # Read temperature from Pico's internal sensor
    adc_value = SENSOR.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    temperature = round(temperature, 2)
    return temperature

def Send_temp(temp):
    # Send temperature to Thingspeak
    thingspeak_http = f'https://api.thingspeak.com/update?api_key={APIKEY}&field1={temp}'
    response = requests.get(thingspeak_http)
    response.close()
    print(temp)
    return None

def Main():
    Wificon()
    while True:
        temperature = Read_temp()
        Send_temp(temperature)
        time.sleep(60)  # Set interval for measurement (s)

Main()