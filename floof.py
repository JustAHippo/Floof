# I know what you guys are about to say... "YOU SAID NO UPDATES", you loudly shriek! Guess what?! I got bored. Here you go. It sucks really bad and can be optimized a lot. Just look at it wow cool plz lol.
# Someone commit to my shitty sniper plz
import requests
import aiohttp
import time
import os
import datetime
import asyncio
f = open("bearer.txt", "r")
bearerlist = f.readlines()
#os.system('cls')
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
#bearer = input("Bearer: ")
delay = int(input("Delay: "))
droptime = time.mktime(
	datetime.datetime.fromisoformat(
		requests.get(f'https://api.nathan.cx/check/{name}').json()['drop_time'][:-1]).replace(
		tzinfo=datetime.timezone.utc).astimezone().timetuple())
async def main():
    headers={"Content-type": "application/json", "Authorization": "Bearer " + line}
    json={"profileName": name}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post("https://api.minecraftservices.com/minecraft/profile", json=json) as r:
            #json_body = await r.json()
            print('Request sent @ ' + str(time.time()) + ' with the code ' + str(r.status))
if droptime + - time.time() > 60:
    print('Sniping ' + name + ' in ' + str(round((droptime + - time.time()) / 60 )) + ' minutes!')
if droptime + - time.time() < 60:
    print('Sniping ' + name + ' in ' + str(round(droptime + - time.time())) + ' seconds!')
time.sleep(droptime + - time.time() - (delay / 1000))
for line in bearerlist:
	loop = asyncio.get_event_loop()
	coroutines = [main() for _ in range(6)]
	results = loop.run_until_complete(asyncio.gather(*coroutines))
