from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

my_url = 'https://jasuteren.cz/'

uClient = req(my_url)

page_html = uClient.read()

page_soup = soup(page_html, 'html.parser')
uClient.close()
containers = page_soup.findAll("div",{"class":"event"})

theater = "teren"
teren_output = []
month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
month_dict = dict(zip(month_name,month_num))
year = page_soup.footer.text.split("©")[1].strip().split(",")[0]

for container in containers:
  dates = container.findAll("div",{"class":"date"})[0].text.strip().split()
  month_man = dates[1].split(".")[1]
  month = str(month_dict[month_man])
  day = dates[1].split(".")[0]
  time = dates[2]+":00"
  title = container.find("a",{"class":"title"}).find("span").text.strip()
  info = container.find("a",{"class":"title"})["href"]

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater', 'date', 'title', 'info']
  teren_row = dict(zip(keys, [theater, date, title, info]))
  teren_output.append(teren_row)