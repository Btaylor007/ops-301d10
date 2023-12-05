import os

# Declaring variables
username = os.popen('whoami').read().strip()
ip_address = os.popen('ip a').read().split('inet ')[1].split('/')[0]
hardware_info = os.popen('lshw -short').read()
