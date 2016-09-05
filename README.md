# SoccerStatisticTool


###HOW TO RUN WEEKLY RESULTS:
To modify the teams goals add flag -m and flag -g (goals) followed by week to modify: 
```
python weeklyResults.py -m -g 10
```

To modify the game's expected team to win the game add flag -m and flag -e (expected) followed by week to modify: 
```
python weeklyResults.py -m -e 10
```

To view the whole week's results specify the week number:
```
python weeklyResults.py 10
```

To write to write a week's matches specify the -w flag folled by that weeks date
```
python main.py 09-09-2016
```