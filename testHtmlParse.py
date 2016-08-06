from lxml import html
from bs4 import BeautifulSoup
import requests


#url = 'http://www.univision.com/deportes/futbol/liga-mx-apertura/calendario'
url = 'http://espndeportes.espn.com/futbol/calendario/_/liga/mex.1'
url = 'http://espndeportes.espn.com/futbol/fixtures/_/fecha/20160729/liga/mex.1'

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

lines = soup.find_all("tr", {"class":["odd","even"]})

#print soup.prettify
for line in lines:
    print line.contents[0].find_all("a", {"class":"team-name"})[0].find_all("span")[0].text + ' ' + \
    line.contents[0].find_all("span", {"class":"record"})[0].find_all("a")[0].text + ' ' + \
    line.contents[1].find_all("a", {"class":"team-name"})[0].find_all("span")[0].text


