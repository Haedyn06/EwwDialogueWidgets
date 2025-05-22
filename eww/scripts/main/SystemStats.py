#!/usr/bin/env python3
import os
import sys
import subprocess
import json

def get_cpu_bar():
    result = subprocess.run(["top", "-bn1"], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "Cpu(s)" in line:
            parts = line.split()
            return int(float(parts[1].replace(",", ".")) + float(parts[3].replace(",", ".")))

def get_ram_bar():
    result = subprocess.run(["free"], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "Mem:" in line:
            parts = line.split()
            return int(float(parts[2]) / float(parts[1]) * 100)

def get_gpu_bar():
    try:
        result = subprocess.run(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"], 
                                capture_output=True, text=True)
        return int(result.stdout.strip())
    except Exception:
        return 0

def get_cpu_usage():
    cpu_usage = get_cpu_bar()
    return f"CPU Usage: {cpu_usage}%"

def get_ram_usage():
    ram_usage = get_ram_bar()
    return f"RAM Usage: {ram_usage}%"

def get_gpu_temp():
    gpu_temp = get_gpu_bar()
    return f"GPU Temp: {gpu_temp}°C"

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg == "--cpuBar":
        print(get_cpu_bar())
    elif arg == "--ramBar":
        print(get_ram_bar())
    elif arg == "--gpuBar":
        print(get_gpu_bar())
    elif arg == "--cpu":
        print(get_cpu_usage())
    elif arg == "--ram":
        print(get_ram_usage())
    elif arg == "--gpu":
        print(get_gpu_temp())
    elif arg == "--all":
        data = {
            "cpu_usage": get_cpu_usage(),
            "ram_usage": get_ram_usage(),
            "gpu_temp": get_gpu_temp()
        }
        print(json.dumps(data, indent=4))
