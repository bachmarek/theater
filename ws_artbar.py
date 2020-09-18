from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

my_url = "https://www.druhypad.cz/program/"
base_url = "https://www.druhypad.cz/"

uClient = req(my_url)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")
uClient.close()
containers = page_soup.findAll("div", {"class": "col-md-8"})
dates = page_soup.find("h2", {"class": "title"})

theater = "artbar"
year = dates.find("a").text.split(" ")[1]
artbar_output = []

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
month_man = str.lower(dates.find("a").text.split(" ")[0])
month = str(month_dict[month_man])

for container in containers:
    ## Den
    dates_container = container.findAll("p", {"class": "date"})
    day = dates_container[0].text.split(".")[0].split(" ")[1]

    ## Čas
    time_base = dates_container[0].text.split()[2]
    time = time_base + ":00"

    ## Název hry
    title = container.findAll("h2")[0].text

    ## Info
    info_link = container.find("h2").find("a")["href"]
    info = base_url + info_link

    ## Date string
    date_string = time + " " + day + " " + month + " " + year
    date = dt.strptime(date_string, "%X %d %b %Y")

    ## Output
    keys = ["theater", "date", "title", "info"]
    artbar_row = dict(zip(keys, [theater, date, title, info]))
    artbar_output.append(artbar_row)