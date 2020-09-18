from bs4 import BeautifulSoup as soup
import requests as req
from datetime import datetime as dt

my_url = 'https://divadlobolkapolivky.cz/program/'

html = req.get(my_url)

page_html = html.text

page_soup = soup(page_html, 'html.parser')
containers = page_soup.findAll("div",{"class":"events-item "})

theater = "bolek"
bolek_output = []

month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
month_dict = dict(zip(month_name,month_num))

year = page_soup.find("h2").text.split(" ")[1]

for container in containers:
  month_man = container.find("div",{"class":"events-date"}).text.strip().split(".")[1].strip()
  month = str(month_dict[month_man])
  day = container.find("div",{"class":"events-date"}).text.strip().split(".")[0].strip()
  time = container.find("div",{"class":"events-date"}).text.strip().split()[3]+":00"
  title = container.find("h2", {"itemprop":"name"}).text.strip()
  info = container.a["href"]

## Date string
  date_string = time +" "+ day +" "+ month +" "+ year
  date = dt.strptime(date_string, "%X %d %b %Y")

## Output
  keys = ['theater', 'date', 'title', 'info']
  bolek_row = dict(zip(keys, [theater, date, title, info]))
  bolek_output.append(bolek_row)
print(bolek_output)