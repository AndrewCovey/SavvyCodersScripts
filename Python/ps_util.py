# We are going to use the psutil command to format a script to check these items.  cpu times, cpu percentatge, disk partion's, users and net connections.  
# You may have to do some extra modification to make the ouput be more readable.


import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    """Scale bytes to its proper format (e.g. KB, MB, GB)."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_info():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def boot_time_info():
    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.strftime('%Y-%m-%d %H:%M:%S')}")

def cpu_info():
    print("="*40, "CPU Info", "="*40)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency: {psutil.cpu_freq().current:.2f} Mhz")
    print(f"CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def memory_info():
    print("="*40, "Memory Info", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")

def disk_info():
    print("="*40, "Disk Info", "="*40)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        print(f"  Total Size: {get_size(usage.total)}")
        print(f"  Used: {get_size(usage.used)}")
        print(f"  Free: {get_size(usage.free)}")
        print(f"  Percentage: {usage.percent}%")

def network_info():
    print("="*40, "Network Info", "="*40)
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

def main():
    system_info()
    boot_time_info()
    cpu_info()
    memory_info()
    disk_info()
    network_info()

if __name__ == "__main__":
    main()
