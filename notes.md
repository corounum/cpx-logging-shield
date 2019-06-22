# 20190614

Following instructions here:
https://docs.micropython.org/en/latest/esp32/tutorial/intro.html
https://micropython.org/download#esp32

Grabbed firmware
wget https://micropython.org/resources/firmware/esp32-20190615-v1.11-45-g14cf91f70.bin

## Erased flash
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash

## Upload new interpreter
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32-20190615-v1.11-45-g14cf91f70.bin

This produced output:

	esptool.py v2.6
	Serial port /dev/cu.SLAB_USBtoUART
	Connecting........_
	Chip is ESP32D0WDQ6 (revision 1)
	Features: WiFi, BT, Dual Core, Coding Scheme None
	MAC: 30:ae:a4:24:a1:2c
	Uploading stub...
	Running stub...
	Stub running...
	Changing baud rate to 460800
	Changed.
	Configuring flash size...
	Auto-detected Flash size: 4MB
	Compressed 1169696 bytes to 731868...
	Wrote 1169696 bytes (731868 compressed) at 0x00001000 in 17.7 seconds (effective 527.4 kbit/s)...
	Hash of data verified.
	
	Leaving...
	Hard resetting via RTS pin...


Every time I did this, it disappeared from the Mac. I had to unplug/plug to get back the serial port.

# Tutorial

At this point, I used Serial.app to connect to the device, and had a Python REPL. 
The ESP32 docs suggested going to the ESP8266 tutorial because they are so similar.

https://docs.micropython.org/en/latest/esp8266/tutorial/index.html#esp8266-tutorial

# 20190615

Setup a python venv for the installation of tools to work with the ESP32.

This allowed me to install ampy. This is a tool to transfer files to/from the ESP32.

https://github.com/pycampers/ampy

## IMPORTANT
It may have been critical to install the most recent serial drivers.
https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

For reasons I do not understand, after installing the newest drivers, my Serial app connected to the device.
That said... it may be that I unplugged/plugged.

I setup an upload script so that we can upload any Python file as "main.py." 
I also set main.py to be ignored in .gitignore. 

This means we should never write a "main.py." It won't work if main.py exists.

I explored having an address like "backyard.local" for the ESP32 when it is working as an access point (AP). It turns out that library support for this is poor. We should assume our infrastructure will have a  Raspberry Pi running as an access point/hub, and everyone will attach to that. 

## NOTE
I had a busy loop in my MQTT testing. I was unable to use esptool to upload code, I think, because the ESP32 was never pausing.

I've added a sleep in my loop. 

I also had to reflash the whole thing to reset it.

