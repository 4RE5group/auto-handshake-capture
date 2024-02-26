import os
import subprocess
import time
import csv

def attack(SSID, ESSID, channel, interface):
        os.system(f"sudo iwconfig {interface} channel {channel}")

        subprocess.Popen([])

def getAPList(interface):

        os.system("rm -rf out-*.csv")
        subprocess.Popen(['sudo', 'airodump-ng', interface, '-w', 'out', '--output-format', 'csv'])

        time.sleep(10)

        os.system("sudo pkill -f airodump-ng")
        os.system("clear")

        with open('out-01.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                        for row in reader:
                                print(row[None][0], row[None][13])
                except:
                        pass

interface="wlan1mon"
getAPList(interface)
