import xml.etree.ElementTree as ET
tree = ET.parse('resultados.xml')
root = tree.getroot()

for child in root.findall('jornada10'):
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

