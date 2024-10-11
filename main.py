# Write a Python script that performs the following
# Monitors the system's CPU and memory usage in real-time (sample every 5 seconds).
# Logs the CPU and memory usage to a text file every minute.
# The script should include error handling for scenarios like insufficient 
# permissions to access system resources or write to the file.

import psutil
from multiprocessing import Process

def log_cpu_memory_usage_to_stdo(cpu_usage_fun, memory_usage_fun, interval):
    """
    Logs the cpu and memory usage to standard output 
    cpu_usage_fun: function that returns CPU usage as a percentage
    memory_usage_fun: function that returns memory usage
    interval: logging delay in seconds
    """
    while True:
        try:
            print(f"{cpu_usage_fun(interval=interval)} \t \t {memory_usage_fun().percent}")
        except:
            print("An error occured.")
            break

def log_cpu_memory_usage_to_file(file_name, cpu_usage_fun,  memory_usage_fun, interval):
    """
    Logs the cpu and memory usage to a file 
    file_name: the name of the file to write CPU and memory usage
    cpu_usage_fun: function that returns CPU usage as a percentage
    memory_usage_fun: function that returns memory usage
    interval: logging delay in seconds
    """
    while True:
        try:
            with open(file_name, "a") as file:
                file.write(f"\n {cpu_usage_fun(interval=interval)} \t \t {memory_usage_fun().percent} \n")
        except OSError as e:
            print(e)
            break
        except IOError as e:
            print(e)
            break
        except PermissionError as e:
            print(e)
            break

if __name__ == '__main__':
    print("CPU(%) usage \t Memory(%) usage")
    cpu_usage_method = psutil.cpu_percent
    memory_usage_method = psutil.virtual_memory
    log_to_stdo_process = Process(target=log_cpu_memory_usage_to_stdo, args=(cpu_usage_method, memory_usage_method, 5))
    log_to_file_process = Process(
        target=log_cpu_memory_usage_to_file, 
        args=("/Users/emmanuelmaungawork/Desktop/system-resources-monitor.txt", cpu_usage_method, memory_usage_method, 5)
        )
    log_to_stdo_process.start()
    log_to_file_process.start()                 