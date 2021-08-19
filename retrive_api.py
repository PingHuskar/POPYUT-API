import requests
import time
import datetime
import io
import webbrowser

now = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

url = "https://api.prayut.click/leaderboard"
a = requests.get(url).text
exec (f"data = {a}")

with io.open('log.txt','a+',encoding='utf-8') as f:
    f.write(f"{now},total,{data['total']}\n")
    f.write(f"{now},rate,{data['rate']}\n")
    f.write(f"{now},online,{data['online']}\n")
    
    for i in data['guilds']:
        f.write(f"{now},{i['name']},{i['total']}\n")
    
    f.close()
webbrowser.open("Your Google Sheets URL")
