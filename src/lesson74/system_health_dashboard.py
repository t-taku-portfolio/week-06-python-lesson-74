import datetime
import json
import zoneinfo
from pathlib import Path

import psutil


def check_disk_health(threshold_percent: float = 85.0) -> dict:
    '''Inspect the partition mounted at root and return the usage percentage.
    If the usage parcentage exceeds the given threshold, it returns is_unhealthy True'''
    # Returns volume stats and an alert flag if usage exceeds threshold.

    # Capture root disk metrics
    root_disk_usage = psutil.disk_usage('/')

    # Capture mount c drive metrics
    c_drive_disk_usage = psutil.disk_usage('/mnt/c')

    # Evaluate the most heavily used disk
    used_disk_max_percent = max(round(root_disk_usage.percent, 2), round(c_drive_disk_usage.percent, 2))

    # Return 
    return {
        "disk_used_percent" : used_disk_max_percent,
        "is_unhealthy" : used_disk_max_percent > threshold_percent
        }

def check_memory_cpu(threshold_percent: float = 80.0) -> dict:
    '''Returns RAM stats and an alert flag if usage exceeds threshold.'''

    cpu_usage = psutil.cpu_percent(interval= 1)
    memory_info = psutil.virtual_memory()

    return {
        "cpu_load_percent": cpu_usage,
        "ram_used_gb": round(memory_info.used / (1024**3), 2),
        "ram_used_percent": memory_info.percent,
        "is_unhealthy": cpu_usage > threshold_percent
    }

def get_top_cpu_process(count: int = 5) -> list:
    '''Returns the top CPU consumers.'''

    # Initialize list every time
    procs = []

    try:
        # Retrieve iterator that has "info" dict including the attributes
        # All attributes are listed in the psutil's the as_dict() section
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                procs.append(proc.info)

            # Catch exceptions for each process's information so as not to skip the entire iteration
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(e)

        # Sort the list by CPU percent
        sorted_procs = sorted(procs, key= lambda proc: proc['cpu_percent'] or 0, reverse= True)
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(e)

    # Return top CPU in range of "count"
    return sorted_procs[:count]

def generate_health_report() -> dict:
    '''Combines all checks into a single structured summary dictionary.'''

    volume_stats = check_disk_health()
    for key in volume_stats:
        print(f'{key}: {volume_stats[key]}')

    memory_stats = check_memory_cpu()
    for key in memory_stats:
        print(f'{key}: {memory_stats[key]}')

    top_cpu_process = get_top_cpu_process() 
    print(top_cpu_process)

    # Combine all checks into single structured summary
    return {
        "volume_stats": volume_stats,
        "memory_stats": memory_stats,
        "top_cpu_process": top_cpu_process
    }

def create_report_json(target_dir: str) -> str:
    data = generate_health_report()
    JAPAN_TOKYO = zoneinfo.ZoneInfo('Asia/Tokyo')
    timestamp = datetime.datetime.now(JAPAN_TOKYO).strftime('%Y_%m_%d')
    file_path = Path(target_dir) / f'health_report_{timestamp}.json'
    try:
        with open(file_path, 'w') as f:
            json.dump(obj=data, fp= f, indent= 4)
    except FileNotFoundError:
        print('Could not reach target path')
        raise
    return file_path

if __name__ == '__main__':
    print(f'[DONE] Create health report at {create_report_json(Path.cwd())}')