from datetime import datetime, timedelta
today = datetime.now()
_5days_ago = today - timedelta(days=5)
print(_5days_ago.strftime("%A"))