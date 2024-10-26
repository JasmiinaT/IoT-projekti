import network
import time
import machine
import requests

# Replace "?" with your own credentials
ssid = '??????'
password = '??????'
APIKEY = "T9S32VCI1I6CH7HY"

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

def Read_temp():
    # Read temperature sensor

    return temperature

def Read_ref()
    # Read reference temperature
    
    return ref_temp

def Send_temp(temp, ref):
    # Send temperature to Thingspeak
    thingspeak_http = f'https://api.thingspeak.com/update?api_key={APIKEY}&field1={temp}&field2={ref}'
    response = requests.get(thingspeak_http)
    response.close()
    print(temp)
    return None

def Main():
    Wificon(ssid, password)
    while True:
        temperature = Read_temp()
        ref_temp = Read_ref()
        Send_temp(temperature, ref_temp)
        time.sleep(60)  # Set interval for measurement (s)

Main()