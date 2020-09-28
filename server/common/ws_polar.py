from bs4 import BeautifulSoup as soup
import requests as req
from datetime import datetime as dt

def polar():
  my_url = 'https://divadlopolarka.cz/program/'

  html = req.get(my_url)

  page_html = html.text

  page_soup = soup(page_html, 'html.parser')
  containers = page_soup.findAll("div",{"class":"program__left-part"})

  theater = "polar"
  polar_output = []

  month_num = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  month_name = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
  month_dict = dict(zip(month_name,month_num))

  ## Rok
  year = page_soup.find("h1",{"class":"underline"}).text.strip().split()[1]

  for container in containers:
    canceled = container.findChild("div", {"class":"program__canceled"})
    if canceled == None:
    ## Měsíc
      month_man = container.strong.text.split("/")[1]
      month = str(month_dict[month_man])

    ## Den
      day = container.find("strong").text.split("/")[0]
    ## Time
      time = container.find("span").text.strip().split()[-1].replace(".", ":")+":00"
    ## Název  
      title_container = container.find("a")
      if title_container.span:
        title_container.span.extract()
      title = title_container.text.strip()
    ## Info
      info = container.find("a")["href"]

    ## Date string
      date_string = time +" "+ day +" "+ month +" "+ year
      date = dt.strptime(date_string, "%X %d %b %Y")
      
      ## Output
      keys = ['theater', 'date', 'title', 'info']
      polar_row = dict(zip(keys, [theater, date, title, info]))
      polar_output.append(polar_row)
    else: 
      None
  return polar_output