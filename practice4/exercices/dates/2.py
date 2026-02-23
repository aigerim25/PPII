from datetime import datetime, timedelta
today = datetime.now()
print("Today:", today.strftime("%A"))
tommorow = today + timedelta(days=1)
print("Tomorrow:", tommorow.strftime("%A"))
yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday.strftime("%A"))

