from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)
soup = bs(page.text,"html.parser")
table = soup.find("table")
templist = []
tablerows = table.find_all("tr")
for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    templist.append(row)
starnames = []
distance = []
mass = []
radius = []
lum = []
for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])
df = pd.DataFrame(list(zip(starnames,distance,mass,radius,lum)),columns = ["starnames","distance","mass","radius","lum"])
print(df)
df.to_csv("bright_stars.csv")