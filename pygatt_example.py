import pygatt.backends

adapter = pygatt.backends.BGAPIBackend()
device = adapter.connect("AA:BB:CC:DD:EE:FF")
value = device.char_read("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b")