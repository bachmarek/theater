from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt
import re


def depog():
    my_url = "https://www.depog.com/#program-terminy"
    uClient = req(my_url)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    uClient.close()
    containers = page_soup.findAll("a", {"class": "dates__block"})

    ## Divadlo
    theater = "depog"
    year = str(dt.now()).split("-")[0]

    ## Output array
    depog_output = []

    for container in containers:

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
        month_name = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        month_dict = dict(zip(month_name, month_num))
        dates_container = (
            container.find("p", {"class": "dates__date"})
            .text.strip()
            .split(".")[1]
            .strip()
        )
        month = str(month_dict[dates_container])

        ## Day
        day = (
            container.findAll("p", {"class": "dates__date"})[0]
            .text.split(".")[0]
            .strip()
        )

        ## Čas
        time_container = container.findAll("p")[1].text.strip().split(" ")[-1]
        time = re.sub("[^0-9]", ":", time_container) + "00"

        ## Název hry
        title = container.findAll("h3", {"class": "dates__name"})[0].text.strip()

        ## Info
        info = "https://www.depog.com/"

        ## Date string
        date_string = time + " " + day + " " + month + " " + year
        date = dt.strptime(date_string, "%X %d %b %Y")

        ## Output
        keys = ["theater", "date", "title", "info"]
        depog_row = dict(zip(keys, [theater, date, title, info]))
        depog_output.append(depog_row)
    return depog_output
