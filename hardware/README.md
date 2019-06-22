## CPX Logging Shield

This "shield" for the Circuit Playground Express integrates:

* an ESP32 WROOM-32D module for capturing data via serial (or, eventually, I2C), storing that data (on the integrated 4MB flash), and presenting the data back via WiFi
* A BME680 temperature/pressure/VOC/eCO2 sensor
* A PCF8523 real time clock (for timestamping readings) and CR1220 battery (for clock retention)

In addition, a QUIIC connector is included for attaching Sparkfun-produced I2C modules. The bottom-mounted FTDI header can be soldered for development, and used as pogopin landing pads for production with the appropriate jig.

The board ONLY takes power from a connected CPX; it draws from VOUT, which is EITHER connected to USB or battery. The shield has its own AP2112 voltage regulator.

It is expected that the combination of a CPX and this shield might run for at most days. The shield attempts to sleep between readings, but it is known that this is potentially a "short life" sensing platform suitable for educational purposes, but not long-life monitoring in research contexts.

The following README text acknowledges that the board design herein leverages the excellent work of [Adafruit Industries](https://adafruit.com), and as a derivative work, is provided under a compatible, open license.

## Adafruit-Circuit-Playground-Express-PCB

PCB files for the Adafruit Circuit Playground Express

This is the PCB files for the Adafruit Circuit Playground
Format is EagleCAD schematic and board layout

For more details, check out the product page at

   * http://www.adafruit.com/products/3333

Adafruit invests time and resources providing this open source design, 
please support Adafruit and open-source hardware by purchasing 
products from Adafruit!

Designed by Adafruit Industries.  
Creative Commons Attribution, Share-Alike license, check license.txt for more information
All text above must be included in any redistribution