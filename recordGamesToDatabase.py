import argparse
import os;
os.chdir(os.getcwd() + '/database') # Must change current working direcory to where the config file is located
print os.getcwd()
from database.databaseCalls import getTeamId
os.chdir(os.getcwd()+ '/..')
print os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument("date", help="Date of games you want to add to database.",
                    type=str)
args = parser.parse_args()
print args.date



print getTeamId('America')
