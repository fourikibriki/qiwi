import requests
import xml.etree.ElementTree as et

print("Введите дату (dd/mm/yyyy)")
date = input()
print("Введите название валюты (пример:USD)")
code = input()

name = (
    et.fromstring(requests.get(url=f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}').text)
    .find(f"./Valute[CharCode = '{code}']/Name")
    .text.replace(",", "."))

rate = float(
    et.fromstring(requests.get(url=f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}').text)
    .find(f"./Valute[CharCode = '{code}']/Value")
    .text.replace(",", "."))

Markdown = f"{code}({name}):{rate}"
print(Markdown)

