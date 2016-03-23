import sys
import xml.etree.ElementTree as ET
tree = ET.parse('output.xml')
root = tree.getroot()

jornada = 'jornada10'
week = root.findall(jornada)

def updateTeamGoals():
    game_num = 1
    for w in week:
        for game in w.iter('game'):
            game.set('number', str(game_num))
            game_num += 1
    tree.write('output.xml')

updateTeamGoals()
