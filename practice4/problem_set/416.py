from datetime import datetime, timezone
start = input()
end = input()
date1 = datetime.strptime(start, "%Y-%m-%d %H:%M:%S UTC%z")
date2 = datetime.strptime(end, "%Y-%m-%d %H:%M:%S UTC%z")
start_utc = date1.astimezone(timezone.utc)
end_utc = date2.astimezone(timezone.utc)
diff = end_utc - start_utc
print(int(diff.total_seconds()))
