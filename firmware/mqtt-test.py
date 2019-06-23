# Copyright 2019 Matt Jadud <matt@jadud.com>
# This software is made available under the MIT License.
# https://opensource.org/licenses/MIT

from umqtt.simple import MQTTClient
import network
import time

sta_if = None

def connect():
  global sta_if
  ssid = "Berea24"
  password = "CherryStreet@BellwetherNY"
  # 30:ae:a4:24:a1:2c

  print('connecting to network...')
  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  sta_if.connect(ssid, password)

  tries = 0
  while not sta_if.isconnected() and tries < 50:
    print("... not connected: {0}".format(tries))
    tries += 1
    pass

  print('network config:', sta_if.ifconfig())
  

def main():
  # python3 -c 'from uuid import uuid4; print(uuid4())'
  c = MQTTClient(b"128352e",   
                 b"io.adafruit.com"
                 #port = 8883
                 )
  c.connect()
  c.publish(b"foo_topic", b"hello")
  c.disconnect()

connect()
if sta_if.isconnected():
  main()
else:
  print("Could not connect.")
