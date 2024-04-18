import network
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Connected to Wi-Fi")

# Replace these with your Wi-Fi credentials and Firebase details
