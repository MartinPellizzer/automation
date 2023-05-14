# [summary]

# order: 
# 	less stress
# 	save time
# 	sense of peace
# 	sense of pride
# 	more motivation
# 	more clarity
# 	more concentration

# set time limits + have breaks:
# 	set time limits
# 	have breaks
# 	more productivity
# 	more focus

import os
import random

input_file = 'C:/notes/warrior_thesis/tmp-notes.txt'
output_file = 'C:/notes/warrior_thesis'

dirs = [item for item in os.listdir(output_file) if os.path.isdir(f'{output_file}/{item}')]

with open(input_file) as f:
    lines = f.readlines()


topic = ''
idea = ''

ideas = []

for line in lines:
    line = line.strip()

    if line.startswith('[') and line.endswith(']'):
        line = line[1:-1]
        
        if topic:
            ideas.append([topic, idea])

        topic = line
        idea = '' 
        continue
    
    if topic:
        idea += line

ideas.append([topic, idea])

for idea in ideas:
    dir_selected = ''
    for d in dirs:
        found = False
        if idea[0] in d:
            found = True
            dir_selected = d
            break
    
    if found:
        rnd = -1
        for i in range(10):
            rnd = random.randint(1000000000000000, 9999999999999999)
            if not os.path.exists(f'{output_file}/{dir_selected}/{rnd}.txt'):
                break
        
        if rnd == -1:
            print('*** error ***')
            print(idea[1])
            break

        with open(f'{output_file}/{dir_selected}/{rnd}.txt', 'w') as f:
            f.write(idea[1])
            
    

# for idea in ideas:
#     print(idea)


# for line in lines:
#     print(line)

# for f in os.listdir('C:/notes/warrior_thesis'):
#     print(f)