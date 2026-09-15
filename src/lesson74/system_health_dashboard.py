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
    return {'disk_used_percent' : used_disk_max_percent,
            'is_unhealthy' : used_disk_max_percent > threshold_percent}

def check_memory_disk(threshold_percent: float = 80.0) -> dict:
    # Returns RAM stats and an alert flag if usage exceeds threshold.

    cpu_usage = psutil.cpu_percent(interval= 1)
    memory_info = psutil.virtual_memory()

    return {"cpu_load_percent": cpu_usage,
            "ram_totla_gb": round(memory_info.total / (1024**3), 2),
            "ram_used_percent": memory_info.percent,
            "is_unhealthty": cpu_usage > threshold_percent}

def get_top_cpu_process(count: int = 5) -> list:
    # Returns the top CPU consumers.

    try:
        proc = psutil.process_iter(['pid', 'name', 'cpu_percent'])
        sorted_pros = sorted(proc, key= lambda proc: proc.info['cpu_percent'] or 0, reverse= True)
        top_cpu = []
        for p in sorted_pros[:count]:
            top_cpu.append(p.info['name'])
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(e)

    return top_cpu

def generate_health_report() -> dict:
    # Combines all checks into a single structured summary dictionary.
    return {}


volume_stats = check_disk_health()
for key in volume_stats:
    print(f'{key}: {volume_stats[key]}')

memory_stats = check_memory_disk()
for key in memory_stats:
    print(f'{key}: {memory_stats[key]}')

print(get_top_cpu_process())