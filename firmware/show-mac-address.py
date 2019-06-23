# Copyright 2019 Matt Jadud <matt@jadud.com>
# This software is made available under the MIT License.
# https://opensource.org/licenses/MIT

import network
import time

# Create station interface
wlan = network.WLAN(network.AP_IF) 
# Get the interface's MAC adddress
mac = wlan.config('mac')      
# The MAC address is a list of bytes. 
# Make it pretty so we can read it.
# https://github.com/micropython/micropython/issues/3115
smac = ""
for ot in list(mac): h = hex(ot); smac += h[2] + h[3]

while True:  
  print(smac)
  time.sleep(2)
