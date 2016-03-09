
import json
with open('LigaMXStadings2016.txt', 'r') as standings:
    teams = []
    for team in standings:
        teams.append(team)

# Each number store as variable
for team in teams:
    for element in team.split('\t'):
        team_name = ''
        standing = []
        try:
            #print element
            int(element.strip())
            standing.append(element)
        except ValueError:
            print "Could not convert data to an integer."

    print json.dumps(team_name)

# Print what it would look like in json

