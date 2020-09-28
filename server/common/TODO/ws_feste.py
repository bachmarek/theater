""" from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt
import re
import sys as prdel

my_url = 'http://www.divadlofeste.cz/program/'

uClient = req(my_url)

page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("a",{"class":"ee-widget-event-name-a three-line"})
dates = page_soup.findAll("span",{"class":"ee-event-datetimes-li-daterange"})
times = page_soup.findAll("span",{"class":"ee-event-datetimes-li-timerange"})

## Divadlo
theater = "feste"

## Měsíc
month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_name = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
month_dict = dict(zip(month_name,month_num))
if len(dates) == 0:
  dates_container = None
else: 
  dates_container = dates[0].text.strip().split()[1]
  month = str(month_dict[dates_container])

## Rok
if len(dates) == 0:
  year = None
else: 
  year = dates[0].text.strip().split()[2]

## Output array
feste_output = []

for container in containers:
## Den
  days = dates[0].text.strip().split()[0]
  day = re.sub("[^0-9]", "", days)

## Čas
if len(times) == 0:
  time_container = None
else: 
  time_container = times[0].text
  time = time_container+":00"

## Název hry
  title = container.text

## Info
  info = container['href']

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater','date', 'title', 'info']
  feste_row = dict(zip(keys, [theater, date, title, info]))
  feste_output.append(feste_row)
 """
