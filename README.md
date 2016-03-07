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

## Connecting using GATTTool

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
