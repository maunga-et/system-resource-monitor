# Operating systems practical assignment

## Problem
Write a Python script that performs the following
- Monitors the system's CPU and memory usage in real-time (sample every 5 seconds).
- Logs the CPU and memory usage to a text file every minute.
- The script should include error handling for scenarios like insufficient permissions to access system resources or write to the file.

## Solution
Used a 3rd-party library called [psutil](https://psutil.readthedocs.io/en/latest/) for the functionality to get CPU and memory usage as percentages. The script starts two processes one for logging the usages to the standard output every 5 seconds and the other to log to a text file every 60 seconds. Used the [multiproccessing](https://docs.python.org/3/library/multiprocessing.html) library which comes with the Python standard library.