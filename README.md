# Auto Handshake Capture
Automated wifi handshake capture using airmon-ng tools

Tested on a RPI zero and a TPU plus TP-Link wifi dongle
Recommended to use on a RPI with no root passwords (script's using sudo often)


<img width="300" src="https://github.com/4RE5group/auto-handshake-capture/assets/71982379/b90be6ab-893a-456d-8330-476248ffc4af" style="transform: rotate(90deg)">



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

## Credits
made with ❤️ by 4re5 group - 2024
