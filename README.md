# System Health Checker

A Python-based system monitoring utility that checks basic computer health and provides warnings when system resources exceed defined limits.

## Features

- Monitors CPU usage
- Monitors RAM usage
- Monitors disk usage
- Checks internet connectivity
- Displays operating system and processor information
- Detects high resource usage
- Provides overall system health status
- Saves health-check results to a log file
- Supports continuous monitoring
- Allows the user to choose the monitoring interval
- Handles invalid user input

## Technologies Used

- Python
- psutil
- Socket
- Platform
- DateTime

## How It Works

The application collects system information using Python libraries and evaluates CPU, RAM, disk and internet connectivity.

If a monitored value crosses the defined threshold, the application generates a warning.

The application can also save each health check to `health_log.txt` for later review.

## How to Run

1. Install Python.
2. Install the required library:

   `pip install psutil`

3. Run the application:

   `python main.py`

4. Select an option from the menu.

## Project Structure

```text
System Health Checker
│
├── main.py
├── health_log.txt
└── README.md