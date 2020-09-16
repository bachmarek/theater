from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt
import re

this = str(dt.today()).split()[0].split("-")
this_month = this[1]
this_year = this[0]
my_url = 'https://www.mdb.cz/program/'+this_year+'-'+this_month

uClient = req(my_url)

page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("div",{"class":"textBox"})

## Divadlo
theater = "mdb"
mdb_output = []

for container in containers:
  label = ""
## Měsíc
  month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
  month_dict = dict(zip(month_name,month_num))
  month_container = container.findAll("p",{"class":"date"})[0].text.split()[1].split('.')[0]
  month = str(month_dict[month_container])

## Den
  day = container.findAll("p",{"class":"date"})[0].text.split()[0].split('.')[0]

## Rok
  year = "2020"

## Čas
  time_container = container.findAll("p",{"class":"date"})[0].text.strip().split()[3]
  time = re.sub("[^0-9]", ":", time_container)+":00"

## Název hry
  title = container.findAll("h3",{"class":"title"})[0].text.strip()

## Info
  info_container = container.findAll("h3",{"class":"title"})
  info_link = info_container[0].find("a")["href"]
  info = "https://www.mdb.cz"+info_link

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

  ## Output
  keys = ['theater', 'date', 'title', 'info']
  mdb_row = dict(zip(keys, [theater, date, title, info]))
  mdb_output.append(mdb_row)