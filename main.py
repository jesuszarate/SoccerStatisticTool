#Call the classes from here 
import argparse
from espnParser import parse, parseDate
import espnParser
import os;
from database.databaseCalls import getTeamId
from database.databaseCalls import insertMatch
import database.databaseCalls
import json

db = database.databaseCalls

parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of the page you want parsed, is the following format mm/dd/yyyy",
                    type=str)
args = parser.parse_args()

espnParser.writeMatchesToFile(args.date)

