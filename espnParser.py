from lxml import html
from bs4 import BeautifulSoup
from mysql.connector import Error
import requests
import argparse


def parseDate(date):
    darr = date.split('/')
    return darr[2] + darr[0] + darr[1]

def parse(date):
    # TODO: Make the league interchangable
    url = 'http://espndeportes.espn.com/futbol/fixtures/_/fecha/' + date + '/liga/mex.1'
    print 'fetching data from...'
    print url

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "lxml")

    lines = soup.find_all("tr", {"class":["odd","even"]})

    for line in lines:
        print line.contents[0].find_all("a", {"class":"team-name"})[0].find_all("span")[0].text + ' ' + \
            line.contents[0].find_all("span", {"class":"record"})[0].find_all("a")[0].text + ' ' + \
            line.contents[1].find_all("a", {"class":"team-name"})[0].find_all("span")[0].text


parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of the page you want parsed, is the following format mm/dd/yyyy",
                    type=str)
args = parser.parse_args()

print args.date
parse(parseDate(args.date))
