import psutil


def byte_to_mb(byte: int) -> int: return int(byte / (1024 * 1024)) 

def check_disk_health(threshold_percent: float = 85.0) -> dict:
    # Returns volume stats and an alert flag if usage exceeds threshold.

    # Capture root disk metrics
    root_disk_usage = psutil.disk_usage('/')

    # Capture mount c drive metrics
    c_drive_disk_usage = psutil.disk_usage('/mnt/c')

    # Evaluate the most heavily used disk
    used_disk_max_percent = max(round(root_disk_usage.percent, 2), round(c_drive_disk_usage.percent, 2))

    # Return 
    return {'disk_used_percent' : used_disk_max_percent,
            'is_unhealth' : used_disk_max_percent > threshold_percent
        }

def check_memory_disk(threshold_percent: float = 80.0) -> dict:
    # Returns RAM stats and an alert flag if usage exceeds threshold.
    return {}

def get_top_cpu_process(count: int = 5) -> list:
    # Returns the top CPU consumers.
    return []

def generate_health_report() -> dict:
    # Combines all checks into a single structured summary dictionary.
    return {}


volume_stats = check_disk_health()
for key in volume_stats:
    print(f'{key}, {volume_stats[key]}')