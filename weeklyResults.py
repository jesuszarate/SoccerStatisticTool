import sys
import xml.etree.ElementTree as ET
#tree = ET.parse('resultados.xml')
tree = ET.parse('output.xml')
root = tree.getroot()

#User picks the week they want to view
# else display first week

# Team abreviations
Teams = {
'V':'Veracruz',
'At':'Atlas',
'S':'Santos',
'Pa':'Pachuca',
'CA':'Cruz Azul',
'Pu':'Puebla',
'Tig':'Tigres',
'Pm':'Pumas UNAM',
'L':'Leon',
'Q':'Queretaro',
'Mor':'Morelia',
'Mon':'Monterrey',
'J':'Jaguares',
'Tij':'Tijuana',
'Tol':'Toluca',
'D':'Dorados',
'Ch':'Chivas',
'Am':'America'}

def viewResults():
    for game in week.findall('game'):
        g = ''
        for team in game.findall('team'):
            goals = team.get('goals')
            name = team.get('name')
            if g == '':
                g += str(goals) + ' ' + str(name) + '\t vs \t'
            else:
                g += str(goals) + ' ' + str(name)
                expected = game.find('expected').text
                print (g + '\tExpected ->\t' + expected).expandtabs(20)

def viewTeam(team_name):
    
    for game in week.findall('game'):
        for team in game.findall('team'):
            name = team.get('name')
            if name == team_name:
                return team

def updateTeamGoals(team_name, goals):
    for w in week:
        for game in w.iter('game'):
            for team in game.iter('team'):
                name = team.get('name')
                if name == team_name:                    
                    team.set('goals', goals)

def updateMatchExpected(match, expected):
    for w in week:
        for game in w.iter('game'):
            if game.get('number') == match:
                ex = game.find('expected')
                ex.text = expected

def writeToFile():
    tree.write('output.xml')

def getTeamList():
    list = ''
    for team in Teams.keys():
        list += team + ' -> ' + Teams[team] + '\n'
    return list

def setWeek(jornada):
    for j in root.findall('jornada'):
        if jornada == j.get('number'):
            return j


def changeTeamGoals(jornada):
    global week
    week = setWeek(jornada)
    
    team_list = getTeamList()

    while True:
        team = raw_input(team_list + '\n To stop: STOP\n'+ 'What team would you like to modify? ')
                
        if team == 'STOP':
            break
                    
        if team in Teams:
            goals = raw_input('How many Goals:  ')
            team_name = Teams[team]
            updateTeamGoals(team_name, goals)
            print (team + ' has been modified ')
            t = viewTeam(team_name)
            print team_name + ' ' + t.get('goals')
        else:
            print '\n********Invalid team name, try again*********\n'
            continue

    writeToFile()

def getWeekMatches(game_num):
    matches = ''
    for game in week.findall('game'):
        g = ''
        for team in game.findall('team'):
            goals = team.get('goals')
            name = team.get('name')
            if g == '':
                g += str(goals) + ' ' + str(name) + '\t vs \t'
            else:
                g += str(goals) + ' ' + str(name)                    
                expected = game.find('expected').text
                matches += game.get('number')+'\t' + g + '\n'
    return matches

def getWeekMatchesDict(game_num):
    global week
    week = setWeek(game_num)
    matches = []
    import pdb; pdb.set_trace()
    for game in week.findall('game'):
        match = []
        for team in game.findall('team'):
            name = team.get('name')
            match.append(name)
        matches.append(match)
    return matches

def changeGameExpected(jornada):
    global week
    week = setWeek(jornada)#root.findall(jornada)

    team_list = getWeekMatches(jornada)

    while True:
        match = raw_input(team_list + '\n To stop: STOP\n'+ 'What match would you like to modify? ')
        
        if match == 'STOP':
            break
                    
        # Check that it's an integer
        try:
            if int(match) > 0 and int(match) <= 9:
                expected = raw_input('What team do you expect to win the match:  ')
                updateMatchExpected(match, expected)
                print ('Match' + match + ' has been modified ')
            else:
                print '\n********Invalid match number, try again*********\n'
                continue
        except:
                print '\n********Invalid match number, try again*********\n'
                continue

    writeToFile()

def addNewWeek():
    
    week_num = raw_input('What\'s the week number')
    jornada = ET.Element('jornada')
    #while True:
        

alen = len(sys.argv)

if alen == 2:
    global week
    jornada =  sys.argv[1]
    week = setWeek(jornada)
    viewResults()

elif alen == 4:
    if sys.argv[1] == '-m': # If user wants to modify the xml
        if sys.argv[2] == '-g': # If user wants to modify goals
            jornada = sys.argv[3]
            changeTeamGoals(jornada)
        elif sys.argv[2] == '-e':
            jornada = sys.argv[3]
            changeGameExpected(jornada)

else:
    message = 'To modify the results add flag -m followed by weed to modify: python resultadosParser.py -m 10\n'
    message += 'To view the whole week\'s results specify the week number: python resultadosParser.py 10'
    print message

    
    
    
