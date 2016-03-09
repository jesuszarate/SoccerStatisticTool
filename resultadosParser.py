import sys
import xml.etree.ElementTree as ET
tree = ET.parse('resultados.xml')
root = tree.getroot()

#User picks the week they want to view
# else display first week
jornada = 'jornada9'
if len(sys.argv) > 1:
    jornada = 'jornada' + sys.argv[1]
    
for child in root.findall(jornada):
    for game in child.findall('game'):
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

