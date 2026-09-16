# System health dashborad

## Feature
- Check disk health
- Check memory disk
- Check top cpu process
- Generate health report
- Run on the virtual environment UV

## How to run
- Need to install uv for run virtual environment


- Run with below command
```bash
uv run python3 src/lesson74/system_health_dashboard.py
```

- Check available locale paths if you want to change the time zone. The OS-provided time zones will be shown here
```bash
 ls /usr/share/zoneinfo/
```

## Built with
- [psutil](https://github.com/giampaolo/psutil) - Cross-platform library for retrieving process information and usage

## RoadMap
- [ ] Rename the feature's subtitle to be benefit-focused
- [x] Implement check_disk_health
- [x] Implement check_memory_disk
- [x] Implement get_top_cpu_process
- [x] Implement generate_health_report
- ~~[ ] Package it as a module that can run everywhere~~

## Refference
- [psutil](https://psutil.readthedocs.io/stable/#psutil.process_iter) : Refferd to the docs for process_iter. The docs explains how to obtain process's attribute.
- [psutil](https://psutil.readthedocs.io/stable/#psutil.Process.as_dict) : Confirmed the attributes to want with this section.
- [geeksforgeeks](https://www.geeksforgeeks.org/python/get-current-timestamp-using-python/) : Read this article for understanding the basic of getting current timestamp.
- [docs.python.org](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH): Understood how to suppy locale to timestamp.now() function.
- [geeksforgeeks](https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/) : Understood how to export json file easily with this "writing" section.