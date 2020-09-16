''' from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

my_url = 'https://divadlo-radost.cz/program'

uClient = req(my_url)

page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("div",{"class":"row text-center mb-1"})
dates = page_soup.findAll("div",{"class":"col-md-10 text-center"})
years = page_soup.findAll("div",{"class":"col text-center py-4"})

## Divadlo
theater = "radost"

## Měsíc
month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
month_dict = dict(zip(month_name,month_num))
dates_container = dates[0].text.strip().split()[1]
month = str(month_dict[dates_container])

## Rok
year = years[0].text.split()[1]

## Output array
radost_output = []

last_day_text = ""
last_day_num = 0

tickets= ""

for container in containers:
## Den
  day_container = container.findAll("div",{"class":"col-md-1 radost-bg-red text-white"})
  if len(day_container) > 0:
    day_text = day_container[0].text
    last_day_text = day_text.split(".")[0]
    day = day_text.split(".")[0]
  else:
    last_day_text = day_text.split(".")[0]

## Čas
  time_container = container.findAll("div",{"class":"col-md-1 text-white text-right"})[0].text
  time = time_container+":00"

## Název hry
  title_container = container.findAll("a")
  title = " ".join(str.split(title_container[0].text))

## Info
  info = container.find("a")['href']

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater','date', 'title', 'info']
  radost_row = dict(zip(keys, [theater, date, title, info]))
  radost_output.append(radost_row)

print(radost_output) '''