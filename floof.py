# I know what you guys are about to say... "YOU SAID NO UPDATES", you loudly shriek! Guess what?! I got bored. Here you go. It sucks really bad and can be optimized a lot. Just look at it wow cool plz lol.
# Someone commit to my shitty sniper plz
import requests
import time
import http.client, json, threading, ssl
from dateutil.parser import isoparse

f = open("bearer.txt", "r")
bearerlist = f.readlines()
thetitle = f"""███████╗██╗░░░░░░█████╗░░█████╗░███████╗  ░██████╗███╗░░██╗██╗██████╗░███████╗██████╗░
██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝  ██╔════╝████╗░██║██║██╔══██╗██╔════╝██╔══██╗
█████╗░░██║░░░░░██║░░██║██║░░██║█████╗░░  ╚█████╗░██╔██╗██║██║██████╔╝█████╗░░██████╔╝
██╔══╝░░██║░░░░░██║░░██║██║░░██║██╔══╝░░  ░╚═══██╗██║╚████║██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░███████╗╚█████╔╝╚█████╔╝██║░░░░░  ██████╔╝██║░╚███║██║██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░  ╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝"""
print(thetitle)
othertext = f"""(╯°o°)╯ Multi-Bearer Edition!"""
print(othertext)
print('Made By a Hippo')
name = input("Name: ")
delay = int(input("Delay: "))
try:
    jj = requests.get(f'https://api.nathan.cx/check/{name}').json()
except Exception:
    print("Unexpected Error")
    exit()

if not jj.get('drop_time'):
    if jj.get('status') and jj['status'] == 'taken':
        print("Error, name taken")
    print("Unexpected Error")
    exit()

droptime = isoparse(jj['drop_time']).timestamp()
e = threading.Event()

def runRequest(line):
    headers = {"Accept": "application/json", "Authorization": "Bearer " + line}
    jsn     = {"profileName": name}
    jsn     = json.dumps(jsn)
    conn    = http.client.HTTPSConnection("api.minecraftservices.com")
    e.wait()
    conn.request("POST", "/minecraft/profile", jsn, headers)
    response = conn.getresponse()
    print("Got answer at", time.time())
    print(response.status, response.reason)
    print(response.read().decode())

if droptime + - time.time() > 60:
    print('Sniping ' + name + ' in ' + str(round((droptime + - time.time()) / 60 )) + ' minutes!')
if droptime + - time.time() < 60:
    print('Sniping ' + name + ' in ' + str(round(droptime + - time.time())) + ' seconds!')

threads = []
for line in bearerlist:
    line = line.strip()
    for i in range(6):
        threads += [threading.Thread(target=runRequest, args=(line, ))]
for t in threads:
    t.start()

time.sleep(droptime + - time.time() - (delay / 1000))
print("Starting requests at", time.time())
e.set()
