# System health dashborad

## Feature
- Check disk health
- Check memory disk
- Check top cpu process
- Generate health report
- Run on the virtual environment UV

## How to run

- Check available locale paths
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
- [ ] Implement generate_health_report
- ~~[ ] Package it as a module that can run everywhere~~

## Refference
- [psutil](https://psutil.readthedocs.io/stable/#psutil.process_iter)
- [psutil](https://psutil.readthedocs.io/stable/#psutil.Process.as_dict)
- [geeksforgeeks](https://www.geeksforgeeks.org/python/get-current-timestamp-using-python/)
- [geeksforgeeks](https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/)