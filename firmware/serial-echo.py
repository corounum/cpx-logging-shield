import machine as M
from utime import ticks_ms, ticks_us
import esp32

if M.reset_cause() == M.DEEPSLEEP_RESET:
    print('I was in such a deep sleep...')
    

# Use for blinkie
pin = M.Pin(13, M.Pin.OUT)
pin.on()

# Set up the UART
uart = M.UART(1, 115200, tx = 17, rx = 16)
uart.init(115200, bits = 8, parity = None, stop = 1, tx = 17, rx = 16, timeout=0)

# Set up sleep/wake
wakey_wakey = M.Pin(12, M.Pin.IN)
esp32.wake_on_ext0(pin = wakey_wakey, level = esp32.WAKEUP_ANY_HIGH)

count = 0
ms = 1
# Initial timeout when waking up.
threshold = 1000 * ms
last = ticks_ms()

while True:
  ch = uart.read(1) 
  if ch is None:
    now = ticks_ms()
    if now - last > threshold:
      print("Yawn: {0}".format(count))
      pin.off()
      M.deepsleep(10000)
  else:
    print(ch)
    count += 1
    # Reset timeout
    last = now
    threshold = 100 * ms
    