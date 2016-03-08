# metawear
Example code for fetching data from MbientLab's "MetaWear C".


## Setup
Substitute *AA:BB:CC:DD:EE:FF* with the device's MAC address.

1. Install [BlueZ] (http://www.bluez.org/).
 ```
 sudo apt-get update
 sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
 wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.37.tar.xz
 tar xf bluez-5.37.tar.xz
 cd bluez-5.37
 ./configure --disable-systemd --enable-tools
 make
 sudo make install
 sudo cp ./src/bluetoothd /usr/local/bin/
 sudo /usr/bin/install -c tools/btmgmt /usr/bin/btmgmt
 ```
 
2. Make sure the Bluetooth dongle is running.
 ```
 sudo hciconfig hci0 up
 ```
 
3. Enable Blueooth Low Energy.
 ```
 sudo btmgmt le on
 ```
 
4. Add device to whitelist.
 ```
 sudo hcitool lewladd AA:BB:CC:DD:EE:FF
 ```

## Connect using GATTTool

1. Connect to device.
  ```
  sudo gatttool -b AA:BB:CC:DD:EE:FF -I -t random
  [AA:BB:CC:DD:EE:FF][LE]> connect
  ```

2. Read temperature value.
  ```
  [AA:BB:CC:DD:EE:FF][LE]> char-read-hnd 0x001f
  Characteristic value/descriptor: 04 81 00 ca 00
  ```

## Connect using [pygatt] (https://github.com/peplin/pygatt)
1. Install `pygatt`
  ```
  sudo pip install pygatt
  sudo pip install pexpect
  ```
  
2. Change MAC address in `pygatt_example.py` and run the script with `python pygatt_example.py`

## Ambient Light Sensor
To measure the ambient light with an external sensor a light dependant resistor (LDR) is used. Connect the LDR to the MetaWear board according to the provided schematics and read the vlaues from GPIO 0 pin.
![Connect external LDR to MetaWear C](ambient_light_layout.png?raw=true "LDR Schematics")
The actual values depend on the used resistor, on the LDR and on the applied voltage. For the case of MetaWear C the voltage is `V=3[V]`. The values can also be converted to [lux] (https://en.wikipedia.org/wiki/Lux) using [these] (http://emant.com/316002.page) instructions.

====
### Resources
* https://learn.adafruit.com/introduction-to-bluetooth-low-energy/introduction
* https://learn.adafruit.com/bluefruit-le-python-library/overview
* http://www.bluez.org/
* http://emant.com/316002.page
* https://mbientlab.com/metawear/
* https://mbientlab.com/docs/MetaWearCPSv0.5.pdf
* https://github.com/peplin/pygatt
