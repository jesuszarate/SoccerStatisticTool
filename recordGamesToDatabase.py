import argparse
from espnParser import parse
import os;
from database.databaseCalls import getTeamId
from database.databaseCalls import insertMatch
import json

parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of games you want to add to database.",
                    type=str)
args = parser.parse_args()
#print args.date

os.chdir(os.getcwd() + '/database') # Must change current working direcory to where the config file is located
print getTeamId('America')

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

    


    
