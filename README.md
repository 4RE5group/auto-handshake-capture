# Auto Handshake Capture
Automated wifi handshake capture using airmon-ng tools

Tested on a RPI zero and a TPU plus TP-Link wifi dongle
Recommended to use on a RPI with no root passwords (script's using sudo often)


<img width="300" src="https://github.com/4RE5group/auto-handshake-capture/assets/71982379/bf5f2995-3fc8-45d4-bd3f-cb53713e361e">




## installation
`sudo nano /etc/rc.local` and put these lines at the bottom
(this will rename wlan1(dongle interface name) into wlan1mon and put it in monitor mode)
```
sudo ip link set wlan1 down
sudo ip link set wlan1 name wlan1mon
sudo ip link set wlan1mon up
sudo iwconfig wlan1mon mode monitor

sudo python /path/to/file/called/capture.py
# in case you wan't to run it in background add a '&' at the end of above command
```

and then just reboot

## Credits
made with ❤️ by 4re5 group - 2024
