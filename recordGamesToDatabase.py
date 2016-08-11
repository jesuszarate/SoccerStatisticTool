import argparse
from espnParser import parse, parseDate
import os;
from database.databaseCalls import getTeamId
from database.databaseCalls import insertMatch
import database.databaseCalls
import json

db = database.databaseCalls
parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of games you want to add to database.",
                    type=str)
args = parser.parse_args()
#print args.date

os.chdir(os.getcwd() + '/database') # Must change current working direcory to where the config file is located


def saveMatches():
    print '\n\n\n\n'
    for o in parse(args.date):
        homeId =  getTeamId(o['home']['name'])
        homeScore = o['home']['score']
        awayId =  getTeamId(o['away']['name'])
        awayScore = o['away']['score']

        winner = homeScore
        if homeScore < awayScore:
            winner = awayScore

        date = formatDate(args.date)
        insertMatch(homeId, homeScore, awayId, awayScore, winner, date)
        recordRacha(date);        


# Records racha for all games in database
def recordRacha(date):
    matches = db.getMatches(date)

    results = db.getResults()
    for match in matches:
        date = match[6]
        # parameters matchId, currentTeam, win/lose/tie, date
        db.insertRachaEntry(match[0], match[1], compareMatchResults(match[2], match[4], results)[0], date)
        db.insertRachaEntry(match[0], match[3], compareMatchResults(match[4], match[2], results)[0], date)

# Determine winner of the game
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

# Format date for sql query    
def formatDate(date):
    d = date.split('-')
    return  d[2] + d[0] + d[1]
    

#recordRacha(formatDate(args.date))

    


    
