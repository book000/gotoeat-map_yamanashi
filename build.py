# coding: utf-8
import requests
from bs4 import BeautifulSoup
import re
import json
import os
from xml.etree import ElementTree
import time


def main():
    html = requests.get("https://www.gotoeat-yamanashi.jp/archives/merchant")
    soup = BeautifulSoup(html.content, "html.parser")
    tables = soup.findAll("table", {"class": "shopTable"})

    if os.path.exists("merchants.json"):
        json_open = open("merchants.json", "r", encoding="utf8")
        merchants = json.load(json_open)
    else:
        merchants = {
            "data": [],
            "names": []
        }

    for table in tables:
        rows = table.findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            if len(cells) == 0:
                continue
            merchant = cells[0].text.strip()
            merchant_name = re.sub(r"^(.+)\[(.+)\]$", r"\1", merchant).strip()
            merchant_type = re.sub(r"^(.+)\[(.+)\]$", r"\2", merchant).strip()
            merchant_address = cells[1].text.strip()
            merchant_tel = cells[2].text.strip()

            print(merchant_name)

            if merchant_name in merchants["names"]:
                continue

            xml = requests.get(
                "https://www.geocoding.jp/api/?q=" + merchant_address)
            obj = ElementTree.fromstring(xml.text)
            if obj.find("coordinate") != None:
                lat = obj.find("coordinate").find("lat").text
                lng = obj.find("coordinate").find("lng").text
            else:
                lat = None
                lng = None
            time.sleep(10)

            merchants["data"].append({
                "name": merchant_name,
                "type": merchant_type,
                "address": merchant_address,
                "tel": merchant_tel,
                "lat": lat,
                "lng": lng
            })
            merchants["names"].append(merchant_name)

            with open("merchants.json", mode="w", encoding="utf8") as f:
                f.write(json.dumps(merchants, indent=4, ensure_ascii=False))

    print("merchant size: " + str(len(merchants["names"])))

    with open("merchants.json", mode="w", encoding="utf8") as f:
        f.write(json.dumps(merchants, indent=4, ensure_ascii=False))


main()
