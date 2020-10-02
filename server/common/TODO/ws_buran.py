from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

def buran():
  my_url = 'https://buranteatr.cz/program/'

  uClient = req(my_url)

  page_html = uClient.read()

  page_soup = soup(page_html, 'html.parser')
  uClient.close()
  containers = page_soup.findAll("div",{"class":"event"})

  theater = "buran"
  buran_output = []

  month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  month_name = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
  month_dict = dict(zip(month_name,month_num))

  for container in containers:
    dates = container.find("div",{"class":"event-date"}).text.strip().split("~")
    year = dates[0].split("/")[2].strip()
    day = dates[0].split("/")[0].strip()
    month_man = dates[0].split("/")[1].strip()
    month = str(month_dict[month_man])
    time = dates[1].strip().replace(" / ", ":")+":00"
    title = container.find("div", {"class":"event-title"}).text.strip()
    info = container.find("div", {"class":"event-title"}).find("a")["href"]

  ## Date string
    date_string = time +" "+ day +" "+ month +" "+ year
    date = dt.strptime(date_string, "%X %d %b %Y")

  ## Output
    keys = ['theater', 'date', 'title', 'info']
    buran_row = dict(zip(keys, [theater, date, title, info]))
    buran_output.append(buran_row)
  
  return buran_output