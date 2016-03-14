import sys
import xml.etree.ElementTree as ET
tree = ET.parse('output.xml')
root = tree.getroot()

g_ind = 3
e_ind = 4
p_ind = 5

standings = {}
with open('LigaMXStadings2016.txt') as f:
    i = 0
    for line in f:
        if i > 1:
            arr = line.split()        
            if len(arr) > 3:
                standings[arr[1]] = arr[2:]
        i += 1

for s in standings.values():
    print s

plays = 0
g_ind = 1
e_ind = 2
p_ind = 3

rating = {}

for t_name, st in standings.items():
    curr = []
    num_plays = float(st[plays])
    #print num_plays
    #print t_name + ' ' + st[g_ind] +' ' + st[e_ind] +' '+ st[p_ind]    

    curr.append(float(st[g_ind])/num_plays)
    curr.append(float(st[e_ind])/num_plays)
    curr.append(float(st[p_ind])/num_plays)
    rating[t_name] = curr


# Read the matches

for e, s in rating.items():
    print e
    print s

def setWeek(jornada):
    for j in root.findall('jornada'):
        if jornada == j.get('number'):
            return j

def getWeekMatchesDict(game_num):
    matches = []
    
    for week in root.findall('jornada'):
        if game_num == week.get('number'):
            for game in week.findall('game'):
                match = []
                for team in game.findall('team'):
                    name = team.get('name')
                    match.append(name)
                    matches.append(match)
    return matches

for i in getWeekMatchesDict(10):
    print 'here'
    print i
