import argparse
import os;
os.chdir(os.getcwd() + '/database') # Must change current working direcory to where the config file is located
from database.databaseCalls import getTeamId
#os.chdir(os.getcwd()+ '/..') # Change working directory back to where this script is running

parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of games you want to add to database.",
                    type=str)
args = parser.parse_args()
#print args.date


print 'here'
print getTeamId('America')
print 'here end'
