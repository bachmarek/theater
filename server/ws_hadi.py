from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

my_url = 'https://www.hadivadlo.cz/'

uClient = req(my_url)
page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("div",{"class":"block"})

theater = "hadi"
year = "2020"
hadi_output = []

for container in containers:
## Měsíc
  month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
  month_dict = dict(zip(month_name,month_num))
  dates_container = container.findAll("span",{"class":"day-no"})
  month_man = dates_container[0].text.strip().split(".")[1].strip()
  month = str(month_dict[month_man])

## Den
  day = dates_container[0].text.strip().split(".")[0].strip()

## Čas
  time_container = container.findAll("span",{"class":"time day-no"})
  time = time_container[0].text.replace(".", ":")+":00"

## Název hry
  title = container.findAll("h2")[0].text

## Info
  info = container.find("div",{"class":"name"}).find("a")['href']

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater', 'date', 'title', 'info']
  hadi_row = dict(zip(keys, [theater, date, title, info]))
  hadi_output.append(hadi_row)