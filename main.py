import psutil
import socket
import platform
import time
from datetime import datetime


# Check internet connection
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


# Check system health
def check_system():
    # Get system information
    system = platform.system()
    processor = platform.processor()

    # Get current date and time
    current_time = datetime.now()

    # Check CPU
    cpu = psutil.cpu_percent()

    # Check RAM
    ram = psutil.virtual_memory().percent

    # Check Disk
    disk = psutil.disk_usage("C:")
    disk_used = disk.percent

    # Check Internet
    internet = check_internet()

    # Create warning list
    warnings = []

    if cpu > 80:
        warnings.append(f"CPU usage is high: {cpu}%")

    if ram > 80:
        warnings.append(f"RAM usage is high: {ram}%")

    if disk_used > 80:
        warnings.append(f"Disk usage is high: {disk_used}%")

    if not internet:
        warnings.append("Internet connection is unavailable")

    # Display report
    print()
    print("=" * 40)
    print("       SYSTEM HEALTH CHECKER")
    print("=" * 40)

    print("Date & Time      :", current_time)
    print("Operating System:", system)
    print("Processor        :", processor)
    print("CPU Usage        :", cpu, "%")
    print("RAM Usage        :", ram, "%")
    print("Disk Usage       :", disk_used, "%")

    if internet:
        print("Internet         : Connected")
    else:
        print("Internet         : Not Connected")

    print("-" * 40)

    # Display warnings
    if warnings:
        print("Warnings:")

        for warning in warnings:
            print("-", warning)

        print("Overall Status   : ATTENTION NEEDED")

    else:
        print("No problems detected.")
        print("Overall Status   : HEALTHY")

    print("=" * 40)

    # Save report to log file
    with open("health_log.txt", "a") as file:
        file.write("\n")
        file.write(f"Date & Time: {current_time}\n")
        file.write(f"CPU Usage: {cpu}%\n")
        file.write(f"RAM Usage: {ram}%\n")
        file.write(f"Disk Usage: {disk_used}%\n")

        if internet:
            file.write("Internet: Connected\n")
        else:
            file.write("Internet: Not Connected\n")

        if warnings:
            file.write("Overall Status: ATTENTION NEEDED\n")

            for warning in warnings:
                file.write(f"Warning: {warning}\n")

        else:
            file.write("Overall Status: HEALTHY\n")

        file.write("-" * 40 + "\n")


# Display basic system information
def show_system_information():
    system = platform.system()
    processor = platform.processor()

    print()
    print("=" * 40)
    print("       SYSTEM INFORMATION")
    print("=" * 40)
    print("Operating System:", system)
    print("Processor        :", processor)
    print("=" * 40)


# Main menu
while True:

    print()
    print("=" * 40)
    print("       SYSTEM HEALTH CHECKER")
    print("=" * 40)
    print("1. Start System Monitoring")
    print("2. View System Information")
    print("3. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ")

    # Option 1: Start monitoring
    if choice == "1":

        print()

        try:
            interval = int(
                input("Enter monitoring interval in seconds: ")
            )

            if interval <= 0:
                print("Please enter a number greater than 0.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print()
        print("Monitoring started.")
        print("Press Ctrl + C to stop monitoring.")

        try:
            while True:
                check_system()
                time.sleep(interval)

        except KeyboardInterrupt:
            print()
            print("Monitoring stopped.")

    # Option 2: View system information
    elif choice == "2":

        show_system_information()

    # Option 3: Exit
    elif choice == "3":

        print()
        print("Exiting System Health Checker.")
        break

    # Invalid menu choice
    else:

        print()
        print("Invalid choice. Please enter 1, 2, or 3.")