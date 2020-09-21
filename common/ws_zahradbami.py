from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

def zahradbami():
  my_url = "http://www.divadlozahradbami.cz/"

  uClient = req(my_url)

  page_html = uClient.read()

  page_soup = soup(page_html, "html.parser")
  uClient.close()
  containers = page_soup.findAll("div", {"class": "mt-column cf"})
  dates = page_soup.findAll("font", {"class": "wsw-49"})

  theater = "zahradbami"
  zahradbami_output = []

  ## Měsíc
  month_num = [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
  ]
  month_name = [
      "leden",
      "únor",
      "březen",
      "duben",
      "květen",
      "červen",
      "červenec",
      "srpen",
      "září",
      "říjen",
      "listopad",
      "prosinec",
  ]
  month_dict = dict(zip(month_name, month_num))

  dates_container = dates[0].text.split()
  month_man = str.lower(dates_container[1])
  month = str(month_dict[month_man])

  ## Rok
  year = str(dates_container[2])

  for container in containers:
      ## Čas
      time = container.findAll("h3")[1].text + ":00"

      ## Den
      day = container.find("img")["src"].split("/")[-1].split("-")[0].split(".")[0]

      ## Název hry
      title = container.findAll("h3")[0].text.strip()

      ## Info
      if container.find("a") == None:
          info = my_url
      else:
          info = container.find("a")["href"]

      ## Date string
      date_string = time + " " + day + " " + month + " " + year
      date = dt.strptime(date_string, "%X %d %b %Y")

      ## Output
      keys = ["theater", "date", "title", "info"]
      zahradbami_row = dict(zip(keys, [theater, date, title, info]))
      zahradbami_output.append(zahradbami_row)
  return zahradbami_output
