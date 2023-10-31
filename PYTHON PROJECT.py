#!/bin/python3

import platform
import socket
import os
import psutil
import subprocess
import glob
import time

# Script 1
print("Script 1 - OS Version")
print("======================")
time.sleep(2)
os_version = platform.system() + " " + platform.release()
print("OS version:", os_version)
print("\n")

# Script 2
print("Script 2 - IP Addresses")
print("=======================")
time.sleep(2)
private_ip = socket.gethostbyname(socket.gethostname())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
public_ip = sock.getsockname()[0]
sock.close()
def get_default_gateway():
    with os.popen("ip route show default") as output:
        for line in output:
            if "default via" in line:
                return line.split()[2]
    return None
default_gateway = get_default_gateway()
print("Private IP Address:", private_ip)
print("Public IP Address:", public_ip)
print("Default Gateway:", default_gateway)
print("\n")

# Script 3
print("Script 3 - Disk Usage")
print("=====================")
time.sleep(2)
disk_usage = psutil.disk_usage('/')
print("Total Disk Size: {:.2f} GB".format(disk_usage.total / (1024**3)))
print("Free Disk Space: {:.2f} GB".format(disk_usage.free / (1024**3)))
print("Used Disk Space: {:.2f} GB".format(disk_usage.used / (1024**3)))
print("\n")

# Script 4
print("Script 4 - Top 5 Directories and Sizes")
print("==========================")
time.sleep(2)
directories = glob.glob('/home/kali/*/')
du_output = ""
for directory in directories:
    output = subprocess.check_output(['du', '-sh', directory], universal_newlines=True)
    du_output += output
lines = du_output.strip().split('\n')
sorted_lines = sorted(lines, key=lambda x: float(x.split()[0][:-1]), reverse=True)
print("Top 5 directories in /home/kali:")
for line in sorted_lines[:5]:
    size, directory = line.split('\t')
    print(f"{directory}\t{size}")
print("\n")

# Script 5
print("Script 5 - CPU Usage")
print("====================")
time.sleep(2)
while True:
    cpu_percent = psutil.cpu_percent(interval=None)
    print(f"CPU usage: {cpu_percent}%")
    time.sleep(10)
    print("\n")

