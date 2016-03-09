import xml.etree.ElementTree as ET
tree = ET.parse('resultados.xml')
root = tree.getroot()

for child in root.findall('jornada10'):
    for game in child.findall('game'):
        for team in game.findall('team'):
            for goals in team.findall('goals'):
                print team.tag, team.attrib, goals.text

