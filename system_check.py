# system_check.py
import psutil
import datetime

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    timestamp = datetime.datetime.now()
    print(f"[{timestamp}] CPU Usage: {cpu_usage}%")
    print(f"[{timestamp}] Memory Usage: {memory.percent}%")
    return {"cpu": cpu_usage, "memory": memory.percent}

if __name__ == "__main__":
    check_system()
