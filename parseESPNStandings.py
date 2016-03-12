

with open('LigaMXStadings2016.txt') as f:
    for line in f:
        print line.split()[1:]
