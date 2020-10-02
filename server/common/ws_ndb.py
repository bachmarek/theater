from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime as dt


def ndb():
    my_url = "http://www.ndbrno.cz/program"

    uClient = req(my_url)
    page_html = uClient.read()

    page_soup = soup(page_html, "html.parser")
    uClient.close()
    dates = page_soup.findAll("a", {"class": "program_month"})
    program = page_soup.findAll("table", {"id": "program_data"})

    ##Měsíc
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
    dates_container = dates[0].text.strip().split()
    month_man = str.lower(dates_container[0])
    month = str(month_dict[month_man])

    ## Rok
    year = str(dates_container[1])

    ## Output array
    ndb_output = []
    theater = ""

    ## Den číslo
    table_rows = page_soup.find("table", {"id": "program_data"}).findAll(
        "tr", recursive=False
    )
    for i, row in enumerate(table_rows):
        if i == 0:
            continue
        else:
            day = row.td.contents[0].replace(".", "")

            # Main
            containers = row.findAll("div", {"class": "program_inscenation"})
            for container in containers:
                ## Divadlo
                theater = (
                    container.findAll("div", {"class": "item-building"})[0]
                    .text.split(",")[0]
                    .split("-")[0]
                    .strip()
                )
                if len(theater) == 0:
                    break
                if theater == "Malá scéna Mahenova divadla":
                    theater = "Mahenovo divadlo"

                ## Čas
                time_container = (
                    container.findAll("div", {"class": "item-hours"})[0]
                    .text.split("-")[0]
                    .strip()
                )
                time = str(time_container) + ":00"

                ## Název hry
                title = container.findAll("div", {"class": "item-title"})[
                    0
                ].text.strip()

                ## Info
                info = container.find("div", {"class": "item-title"}).find("a")["href"]

                ## Date string
                date_string = time + " " + day + " " + month + " " + year
                date = dt.strptime(date_string, "%X %d %b %Y")

                ## Output
                keys = ["theater", "date", "title", "info"]
                ndb_row = dict(zip(keys, [theater, date, title, info]))
                ndb_output.append(ndb_row)
    return ndb_output
