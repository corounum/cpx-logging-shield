import machine as M
from utime import ticks_ms, ticks_us
import esp32
from time import sleep
from struct import unpack


sleep(1)

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
uart = M.UART(1, 57600, tx = 17, rx = 16)
uart.init(57600, 
          bits = 8, parity = None, stop = 1, 
          tx = 17, rx = 16, 
          timeout_char = 500)

# Set up sleep/wake
wakey_wakey = M.Pin(27, M.Pin.IN)
esp32.wake_on_ext0(pin = wakey_wakey, level = esp32.WAKEUP_ANY_HIGH)

count = 0

# States
WAITING      = const(0x00)
CMD          = const(0x01)
# Numbers
READINT     = const(0x10)
READFLOAT    = const(0x11)

last = ticks_ms()

state = WAITING

intndx = 0
buff32 = bytearray(4)

while True:
  now = ticks_ms()
  b = uart.read(1)
  if b is None:
    # If enough time elapses, go to sleep. 
    if state == WAITING and last - now > 500:  
      print("Yawn...")
      pin.off()
      M.deepsleep(10000)
  # We have a character!
  else:
    print("b: " + str(b) + " " + str(hex(ord(b))) + " " + str(ord(b)))

    if state == WAITING and b == b'I':
      state = READINT
      last = now
      # Reset the buffer and index
      intndx = 0
      buff32 = bytearray(4)
    elif state == READINT and b == b'*':
      intndx = 0
      ndx = 0
      n = 0
      for b in buff32:
        n = n + (b << (8 * ndx))
        # print("conv: " + str(ndx) + " " + str(b) + " " + str(n))
        ndx += 1
      print("Int: {0}".format(n))
      state = WAITING
    elif state == READINT:
      if intndx >= 4:
        # This is no good. Go back to waiting
        # print("INTNDX OUT OF RANGE")
        state = WAITING
      else:
        buff32[intndx] = ord(b)
        intndx += 1

    if state == WAITING and b == b'C':
      state = CMD
      last = now
    elif state == CMD and b == b'S':
      print("CMD SLEEP")
      pin.off()
      sleep(0.1)
      M.deepsleep(10000) 
  