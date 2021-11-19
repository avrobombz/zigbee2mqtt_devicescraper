import os,json,scraper, copy

cwd = os.getcwd()

defaultjson = cwd + "/DEFAULT.json"
pulljson = cwd + "/pull.json"

with open(defaultjson, 'r') as j:
    data = json.load(j)

expose_keys = []
master_list = []
master_dict = data
#### def recurs_keys(dictionary):
    #     for key, value in dictionary.items():
    #         if type(value) is dict:
    #             yield from recurs_keys(value)
    #         else:
    #             yield (key,value)

    # for key, value in recurs_keys(data):
    #     keys.append(key)

for key in data:
    expose_keys.append(key)

url_l = ['https://www.zigbee2mqtt.io/devices/014G2461.html',
'https://www.zigbee2mqtt.io/devices/UK7004240.html',
'https://www.zigbee2mqtt.io/devices/BRT-100-TRV.html',
'https://www.zigbee2mqtt.io/devices/TS0601_thermostat.html',
'https://www.zigbee2mqtt.io/devices/TV01-ZB.html',
'https://www.zigbee2mqtt.io/devices/701721.html',
'https://www.zigbee2mqtt.io/devices/GS361A-H04.html',
'https://www.zigbee2mqtt.io/devices/TS0601_thermostat_1.html']

for i in url_l:
    temp_dict = copy.deepcopy(master_dict)
    
    temp_data = scraper.scrape(i)
    temp_dict['URL'] = i
    temp_dict['MODEL'] = temp_data[0]
    temp_dict['VENDOR'] = temp_data[1]
    temp_dict['DESCRIPTION'] = temp_data[2]
    temp_dict['WHITE_LABEL'] = temp_data[3]
    expose = temp_data[4]

    for i in expose:
        temp_dict['EXPOSES'][i] = 'Y'

    # l = []    
    # l.append(temp_dict)
    master_list.append(temp_dict)
    
    
with open(pulljson, 'w') as jfile:
    jfile.write(json.dumps(master_list,indent=4))

