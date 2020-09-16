from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

my_url = 'http://www.studiomarta.cz/index.php?p=program'
base_url = 'http://www.studiomarta.cz/'

uClient = req(my_url)

page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("div",{"class":"wrapp"})
dates = page_soup.findAll("div",{"id":"cal-navig"})

## Měsíc + Rok
theater = "marta"
month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_name = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
month_dict = dict(zip(month_name,month_num))

dates_container = dates[0].text.strip().split()
month_man = str.lower(dates_container[0])
month = str(month_dict[month_man])

year = str(dates_container[1])

## Output array
marta_output = []

for container in containers:
## Čas + den
  time_container = container.findAll("td",{"class":"den-cas"})
  time_container_split = str.split(time_container[0].text.strip())
  time = str(time_container_split[1])+":00"
  
## Den číslo
  day_num_container = container.findAll("td",{"class":"datum"})
  day_num_split = str.split(day_num_container[0].text.strip())
  day_num = str(day_num_split[0])

## Název hry
  title_container = container.findAll("td",{"class":"title"})
  title = " ".join(str.split(title_container[0].text))

## Info
  info_url = container.find("td",{"class":"title"}).find("a")['href']
  info = base_url+info_url


## Date string
  date_string = time +" "+ day_num +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater', 'date', 'title', 'info']
  marta_row = dict(zip(keys, [theater, date, title, info]))
  marta_output.append(marta_row)