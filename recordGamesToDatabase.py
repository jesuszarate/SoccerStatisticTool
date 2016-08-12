import argparse
from espnParser import parse, parseDate
import os;
from database.databaseCalls import getTeamId
from database.databaseCalls import insertMatch
import database.databaseCalls
import json

parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of games you want to add to database.",
                    type=str)
args = parser.parse_args()
#print args.date

os.chdir(os.getcwd() + '/database') # Must change current working direcory to where the config file is located



def saveMatches():
#os.chdir(os.getcwd()+ '/..') # Change working directory back to where this script is running
    print '\n\n\n\n'
    for o in parse(args.date):
    #print o['home']['name']
        homeId =  getTeamId(o['home']['name'])
        homeScore = o['home']['score']
        awayId =  getTeamId(o['away']['name'])
        awayScore = o['away']['score']

    #print str(homeId) + ' ' + str(homeScore) + ' - ' + str(awayId) + ' ' + str(awayScore)

        winner = homeScore
        if homeScore < awayScore:
            winner = awayScore

        d = args.date.split('-')
        date = d[2] + d[0] + d[1]

        insertMatch(homeId, homeScore, awayId, awayScore, winner, date)


db = database.databaseCalls

def recordRacha():
    matches = db.getMatches()

    results = db.getResults()
    #for match in matches:
    match = matches[1]
    date = match[6]
    db.insertRachaEntry(match[0], match[1], compareMatchResults(match[2], match[4], results)[0], date)
    db.insertRachaEntry(match[0], match[3], compareMatchResults(match[4], match[2], results)[0], date)

def compareMatchResults(teamScore, oponentScore, resultOptions):
    # Team wins
    if teamScore > oponentScore:
        return resultOptions[0]
    # Team loses
    elif teamScore < oponentScore:
        return resultOptions[1]
    # Match is a draw
    else:
        return resultOptions[2]
    

recordRacha()

    


    
