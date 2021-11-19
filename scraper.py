import requests, os, json
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def scrape(url):
    model = []
    expose = []


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
    model = l[1][1]
    vendor = l[2][1]
    description = l[3][1]
    # expose = l[4][1]
    try: white_label = l[6][1]
    except: white_label = ''
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

    return[model,vendor,description,white_label,expose_l]

