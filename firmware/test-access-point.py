# Copyright 2019 Matt Jadud <matt@jadud.com>
# This software is made available under the MIT License.
# https://opensource.org/licenses/MIT

import network
import slimDNS
import time


# Create station interface
ap = network.WLAN(network.AP_IF) 
# Set the AP name
ap.config(essid = "BACKYARD")
ap.ifconfig(('192.168.42.42', 
             '255.255.255.0', 
             '192.168.0.1', 
             '8.8.8.8'))
ap.active(True)

# As it happens, we would need mDNS to have 
# a URL like "backyard.local". This is best 
# accomplished by writing everything in C/C++.
# The reason is that the mDNS libraries exist
# and are mature, whereas there is poor support 
# for mDNS in MicroPython.

# Get the interface's MAC adddress
mac = ap.config('mac')      
# The MAC address is a list of bytes. 
# Make it pretty so we can read it.
# https://github.com/micropython/micropython/issues/3115
smac = ""
for ot in list(mac): h = hex(ot); smac += h[2] + h[3]

while True:  
  print(smac)
  time.sleep(2)
