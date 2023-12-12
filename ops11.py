import psutil

# Get system time information
times = psutil.cpu_times()

# Print the requested information
print("User Mode Time:", times.user)
print("Kernel Mode Time:", times.system)
print("Idle Time:", times.idle)
print("Priority User Mode Time:", times.nice)
print("I/O Wait Time:", times.iowait)
print("Hardware Interrupt Time:", times.irq)
print("Software Interrupt Time:", times.softirq)

# Check if virtual machines are present (Linux only)
if hasattr(psutil.cpu_times(), "steal"):
    print("Virtual Machine Time:", times.steal)

# Check if guest operating systems are present (Linux only)
if hasattr(psutil.cpu_times(), "guest"):
    print("Guest Operating System Time:", times.guest)
