"""
Read all the files currently in the trials directory
take the sum of all the results, and then average them
return these results in sorted frequency, descending
"""

import glob 

results = {}
firstlines = []

total_turns = 0
total_trials = 0
for filename in glob.glob('trials/*.txt'):
    print(filename)
    f = open(filename, 'r')
    first = True
    for line in f:
        if first:
            firstlines.append(line)
            i = 0
            while i < len(line):
                i += 1
                if line[i] == ',':
                    print("here")
                    i += 8
                    break
            j = i 
            while line[j] != '\n':
                j += 1
            total_turns += int(line[i:j])
            total_trials += 1
            first = False
        else:
            # first 3 characters are the property, followed by the number
            prop = line[:3]
            # knock off last 2 characters (/r and /n)
            count = int(line[8:-2]) 
            print((prop, count))
            if prop in results:
                results[prop] += count
            else:
                results[prop] = count

spaces_strings = \
['GO.', 'MED', 'CC1', 'BAL', 'ITX', 'RR1', 'ORI', 'CH1', 'VER', 'CON',
'JAL', 'SCP', 'ECO', 'STA', 'VIR', 'RR2', 'STJ', 'CC2', 'TEN', '.NY',
'FPK', 'KEN', 'CH3', 'IND', 'ILL', 'RR3', 'ATL', 'VEN', '.WW', 'MAR',
'GTJ', 'PAC', 'NCA', 'CC4', 'PEN', 'RR4', 'CH4', 'PPL', 'LTX', 'BWK']
tups = []
for space in spaces_strings:
    tups.append((space, results[space]))
print(tups)

# choose what to call this file based on what is currently there
count = 1 
for filename in glob.glob('Averages*.txt'):
    count += 1
    
filename = "Averages" + "_" + str(count) + ".txt"
f = open(filename, 'w')
f.write("total_trials: " + str(total_trials) + ", total_turns: " + str(total_turns) + "\r\n")

for tup in tups:
    f.write(str(tup[0]) + ' ||| ' + str(tup[1]) + "\r\n")

tups.sort(key=lambda x: -x[1])

f.write('============ sorted ============ ' + "\r\n")
for tup in tups:
    f.write(str(tup[0]) + ' ||| ' + str(tup[1]) + "\r\n")
    





