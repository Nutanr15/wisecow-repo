#!/usr/bin/env python3
import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_NAME = "sshd"  # You can change this if needed

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print(f"[ALERT] High CPU usage detected: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    if memory.percent > MEMORY_THRESHOLD:
        print(f"[ALERT] High Memory usage detected: {memory.percent}%")

def check_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")
    if disk.percent > DISK_THRESHOLD:
        print(f"[ALERT] Low Disk Space detected: {disk.percent}% used")

def check_process():
    found = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == PROCESS_NAME:
            found = True
            break
    print(f"Process '{PROCESS_NAME}': {'Running' if found else 'Not Running'}")
    if not found:
        print(f"[ALERT] Process '{PROCESS_NAME}' not running!")

def main():
    print(f"\n--- System Health Check: {datetime.datetime.now()} ---")
    check_cpu()
    check_memory()
    check_disk()
    check_process()
    print("Check complete.\n")

if __name__ == "__main__":
    main()

