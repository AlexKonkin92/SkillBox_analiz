from datetime import datetime, timedelta
yesterday = (datetime.now() - timedelta(days = 1)).strftime('%Y-%m-%d')
for title, line in stats.items():
    if line[4] == yesterday:
        print(title, line)