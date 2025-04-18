import csv

from assign_1 import exponential_random, normal_random

data  = []
data2 = []
for i in range(500):
    data.append(exponential_random(4))
    data2.append(normal_random(2.5, 0.1))

filename = 'sample.csv'


with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['sampleExp', 'sampleNorm'])  
    for itemExp, itemNorm in zip(data, data2):
        writer.writerow([itemExp, itemNorm])

print(f'Success. File generated: {filename}')
