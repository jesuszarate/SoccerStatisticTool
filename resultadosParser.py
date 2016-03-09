import sys
import xml.etree.ElementTree as ET
tree = ET.parse('resultados.xml')
root = tree.getroot()

jornada = 'jornada9'
week = root.findall(jornada)

#User picks the week they want to view
# else display first week

def viewResults():
    for w in week:
        for game in w.findall('game'):
            g = ''
            for team in game.findall('team'):
                goals = team.get('goals')
                name = team.get('name')
                if g == '':
                    g += str(name) + ' ' + str(goals) + ' vs '
                else:
                    g += str(name) + ' ' + str(goals)
                    expected = game.find('expected').text
                    print g + ' Expected ->\t' + expected

def viewTeam(team_name):
    for w in week:
        for game in w.findall('game'):
            for team in game.findall('team'):
                name = team.get('name')
                if name == team_name:
                    return team

alen = len(sys.argv)
if alen == 2:
    if sys.argv[1] == '-m': # If user wants to modify the xml
        team = raw_input('What team would you like to modify? ')        
        print (team + ' has been modified ')
        t = viewTeam(team)
        print team + ' ' + t.get('goals')

    else:
        jornada = 'jornada' + sys.argv[1]
        viewResults()
#elif alen == 2:
    
    
    
