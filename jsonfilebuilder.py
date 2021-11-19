import requests, os, json
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url_l = ['https://www.zigbee2mqtt.io/devices/014G2461.html',
'https://www.zigbee2mqtt.io/devices/UK7004240.html',
'https://www.zigbee2mqtt.io/devices/BRT-100-TRV.html',
'https://www.zigbee2mqtt.io/devices/TS0601_thermostat.html',
'https://www.zigbee2mqtt.io/devices/TV01-ZB.html',
'https://www.zigbee2mqtt.io/devices/701721.html',
'https://www.zigbee2mqtt.io/devices/GS361A-H04.html',
'https://www.zigbee2mqtt.io/devices/TS0601_thermostat_1.html']

model = []
expose = []

for url in url_l:
    page = requests.get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    bs_r = bs.find('table')
    rows = bs_r.find_all('tr')
    l = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        l.append([ele for ele in cols if ele])

    expose.append(l[4][1])
# model = l[1][1]
# vendor = l[2][1]
# description = l[3][1]
# expose = l[4][1]
expose_str = ''

for i in expose:
    str = i
    str = str.replace(" ","")
    c = "()"
    for a in c:
        str = str.replace(a,",")
    str = str.strip()
    str = str.upper()

    expose_str += str + ','

expose_l = list(expose_str.split(","))
expose_l.sort()
expose_l = list(dict.fromkeys(expose_l))
expose_l = list(filter(None,expose_l))

d = {'MODEL':'','VENDOR':'','DESCRIPTION':'','EXPOSES':{}}
for i in expose_l:
    d['EXPOSES'][i] = ''

cwd = os.getcwd()
defaultjson = cwd + "/DEFAULT.json"

with open(defaultjson, 'w') as jfile:
    jfile.write(json.dumps(d,indent=4))


