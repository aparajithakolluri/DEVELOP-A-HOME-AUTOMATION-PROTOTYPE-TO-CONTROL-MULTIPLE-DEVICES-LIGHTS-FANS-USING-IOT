# This is a basic Python example for controlling lights and fans using the Blynk library.
# You'll need to install the Blynk library: `pip install blynk-library`

from blynk import Blynk
from blynk.co import VirtualPin

# Replace with your actual Blynk Auth Token
BLYNK_AUTH = 'YOUR_BLYNK_AUTH_TOKEN'

# Create a Blynk instance
blynk = Blynk(BLYNK_AUTH)

# Define Virtual Pins for controlling devices
# You can customize these pin numbers as needed
light_pin = VirtualPin(0)
fan_pin = VirtualPin(1)

# Define functions to control devices
def control_light(pin_value):
    """
    Controls the light based on the pin value.
    
    Args:
        pin_value: 0 for off, 1 for on
    """
    if pin_value == '1':
        print("Light turned ON")
        # Add your actual code here to turn the light ON (e.g., control a relay)
    else:
        print("Light turned OFF")
        # Add your actual code here to turn the light OFF
    
def control_fan(pin_value):
    """
    Controls the fan based on the pin value.
    
    Args:
        pin_value: 0 for off, 1 for on
    """
    if pin_value == '1':
        print("Fan turned ON")
        # Add your actual code here to turn the fan ON
    else:
        print("Fan turned OFF")
        # Add your actual code here to turn the fan OFF

# Register the write event handlers for the Virtual Pins
@blynk.on('write', light_pin)
def write_event_handler(value):
    control_light(value[0])

@blynk.on('write', fan_pin)
def write_event_handler(value):
    control_fan(value[0])

# Run the Blynk loop
while True:
    blynk.run()
