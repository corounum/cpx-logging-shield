import machine as M
from utime import ticks_ms, ticks_us
import esp32
from time import sleep

ALPHABET36 = '0123456789abcdefghijklmnopqrstuvwxyz'
alphabet_reverse = dict((char, i) for (i, char) in enumerate(ALPHABET36))

# https://github.com/jpscaletti/base36/blob/master/base36.py
def to36(num, alphabet=None):
    converted = []
    while num != 0:
        num, rem = divmod(num, 36)
        converted.insert(0, ALPHABET36[rem])
    return ''.join(converted) or '0'

def from36(snum, alphabet=None):
    num = 0
    snum = str(snum)
    for char in snum:
        num = num * 36 + alphabet_reverse[char]
    return num

if M.reset_cause() == M.DEEPSLEEP_RESET:
    print('I was in such a deep sleep...')
    

# Use for blinkie
pin = M.Pin(13, M.Pin.OUT)
pin.on()

# Set up the UART
uart = M.UART(1, 115200, tx = 17, rx = 16)
uart.init(115200, bits = 8, parity = None, stop = 1, tx = 17, rx = 16, timeout = 1000, timeout_char = 1000)

# Set up sleep/wake
wakey_wakey = M.Pin(27, M.Pin.IN)
esp32.wake_on_ext0(pin = wakey_wakey, level = esp32.WAKEUP_ANY_HIGH)

count = 0

WAITING = -1
READINT = 0
CMD = 1

state = WAITING
while True:
  # One second timeout
  msg = uart.readline()
  if msg is not None:
    msg = msg.strip()
    print(msg)
    if state == WAITING and msg == b'I':
      print("READINT")
      state = READINT
    elif state == READINT:
      n = int(msg)
      print("Number: {0}".format(n))
      state = WAITING
    elif state == WAITING and msg == b'CMD':
      print("CMD")
      state = CMD
    elif state == CMD:
      if msg == b'SL':
        print("CMD SLEEP")
        pin.off()
        sleep(0.1)
        M.deepsleep(10000)  
  else: # msg was None
    print("Yawn...")
    pin.off()
    M.deepsleep(10000)