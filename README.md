# auto-handshake-capture
Automated wifi handshake capture using airmon-ng tools

Tested on a RPI zero and a TPU plus TP-Link wifi dongle
Recommended to use on a RPI with no root passwords (script's using sudo often)

## installation
`sudo nano /etc/rc.local` and put these lines at the bottom
(this will rename wlan1(dongle interface name) into wlan1mon and put it in monitor mode)
```
sudo ip link set wlan1 down
sudo ip link set wlan1 name wlan1mon
sudo ip link set wlan1mon up
sudo iwconfig wlan1 mode monitor

sudo python /path/to/file/called/capture.py
# in case you wan't to run it in background add a '&' at the end of above command
```

and then just reboot
