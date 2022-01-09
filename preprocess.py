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
header[3] = '兩分命中率'
header[5] = '三分命中率'
header[7] = '罰球命中率'
header[8] += '籃板'
header[9] += '籃板'
header[10] += '籃板'
line.pop(0)

data = pd.DataFrame(line, columns=header)

data['二分出手'] = data['二分'].str.split('-', expand=True).take([0], axis=1)
data['二分命中'] = data['二分'].str.split('-', expand=True).take([1], axis=1)
data['三分出手'] = data['三分'].str.split('-', expand=True).take([0], axis=1)
data['三分命中'] = data['三分'].str.split('-', expand=True).take([1], axis=1)
data['罰球出手'] = data['罰球'].str.split('-', expand=True).take([0], axis=1)
data['罰球命中'] = data['罰球'].str.split('-', expand=True).take([1], axis=1)
data.drop(['二分', '三分', '罰球'], inplace=True, axis=1)
print(data)
line = data.values.tolist()
header = data.columns
# print( data['二分'].str.split('-'))
with open('process_data.csv', mode='w+', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(line)