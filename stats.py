# -*- coding: utf-8 -*-

import sys
from datetime import datetime

data = {}

xq = ''
if len(sys.argv) == 2:
    xq = sys.argv[1]

with open('data.csv', 'r') as f:
    for line in f:
        cols = line.split(',')
        if not cols[0].startswith('https'):
            continue
        if xq and not cols[1].decode('utf8').strip('"').startswith(xq.decode('utf8')):
            continue
        # if cols[2].strip('"').startswith('2室'):
            # continue
        date, price = cols[7], cols[8]
        try:
            price = int(price)
        except:
            continue
        if date not in data:
            data[date] = []
        data[date].append(price)

stats_data = []
for k, v in data.items():
    stats_data.append({
        'dat': datetime.strptime(k, '%Y.%m.%d'),
        'cnt': len(v),
        'max': max(v),
        'min': min(v),
        'avg': sum(v) / len(v),
    })
stats_data.sort(key=lambda x: x['dat'])

import matplotlib.pyplot as plt
x = [sd['dat'] for sd in stats_data]
y = [sd['avg'] for sd in stats_data]
plt.plot(x, y)
plt.show()
