from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt

husa_url = "https://www.provazek.cz/cs/program"
base_url = "https://www.provazek.cz"

uClient = req(husa_url)

page_html = uClient.read()

page_soup = soup(page_html, "html.parser")
uClient.close()
containers = page_soup.findAll("div", {"class": "program__item"})
dates = page_soup.findAll("li", {"class": "program__active"})

## Měsíc
theater = "husa"
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

dates_container = dates[0].text.strip()
month = str(month_dict[dates_container])

# Rok
dates_string = str(dates)


def findYear(dates_string, year_array=None):
    if not year_array:
        year_array = []
    for item in dates_string:
        if item.isdigit():
            year_array.append(item)
    return year_array


year_list = findYear(dates_string)
del year_list[4:]
year = "".join(year_list)

## Output array
husa_output = []

for container in containers:
    ## Čas + den
    when_container = container.findAll("p", {"class": "program__date"})
    when_container_split = str.split(when_container[0].text.strip())
    when = str(when_container_split[1])
    a = when.split(".")
    day_num = a[0]
    time = a[2] + ":00"

    ## Název hry
    title_container = container.findAll("h2", {"class": "program__title"})
    title = " ".join(str.split(title_container[0].text))

    ## Info
    info_url = container.find("h2", {"program__title"}).find("a")["href"]
    info = base_url + info_url

    ## Date string
    date_string = time + " " + day_num + " " + month + " " + year
    date = dt.strptime(date_string, "%X %d %b %Y")

    ## Output
    keys = ["theater", "date", "title", "info"]
    husa_row = dict(zip(keys, [theater, date, title, info]))
    husa_output.append(husa_row)
