import os

# Declare three variables
current_user = os.popen("whoami").read().strip()  # Get username with popen and read
ip_addresses = os.popen("ip a | grep 'inet ' | awk '{print $2}'").read().split()  # Extract all IP addresses with pipes and awk
hardware_summary = os.popen("lshw -short").read()  # Get full hardware summary

# Print information using print() function at least three times
print(f"Current user: {current_user}")
print("Assigned IP addresses:")
for address in ip_addresses:
    print(f"\t- {address}")

if hardware_summary:
    print("Hardware summary:")
    print(hardware_summary)
else:
    print("Unable to retrieve hardware information.")
