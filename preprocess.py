import csv
import os
import pandas as pd
path = ''
file_name = 'game_record'
line = 0
with open(os.path.join(path, file_name + "_output.csv"), mode='r', newline='',  encoding='UTF-8') as f:
        line = list(csv.reader(f))
# print(line)
header = line[0]
line.pop(0)
with open('process_data.csv', mode='w+', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(line)