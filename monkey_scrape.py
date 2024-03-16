import requests
import json
import datetime
import csv

id = int(input("Enter 4 digit log code: "))
r = requests.get("http://monkeylogs.com/API/instance/export/{}".format(id))
mlogs = json.loads(r.content)

guild = mlogs.get('guild_name','Unknown')
raid = mlogs.get('map_id')
time_start = datetime.datetime.fromtimestamp(mlogs.get('start_ts')//1000)
time_end = datetime.datetime.fromtimestamp(mlogs.get('end_ts')//1000)
date = time_start.date()
raid_time = time_end - time_start

if raid == 409:
    raid = 'MC'
elif raid == 469:
    raid = 'BWL'
elif raid == 531:
    raid = 'AQ40'
elif raid == 533:
    raid = 'NAXX'
else:
    raid = 'Unknown'

with open('raid_info.csv', 'w', newline='') as csvfile:
    raid_writer = csv.writer(csvfile, delimiter=',',
             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    raid_writer.writerow([guild,raid,date,raid_time])
    print("Guild:",guild)
    print("Raid:",raid)
    print("Date:",date)
    print("Time:",raid_time)