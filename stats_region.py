# -*- coding: utf-8 -*-

import sys
from datetime import datetime

data = {}

xq_map = dict()
with open('region.csv', 'r') as f:
    for line in f:
        cols = line.split(',')
        xq, reg = cols[0].strip('"'), cols[1].strip('"')
        if reg == 'regionb':
            continue
        if reg not in xq_map:
            xq_map[reg] = set()
        xq_map[reg].add(xq)

if len(sys.argv) == 2:
    region = sys.argv[1]
else:
    for reg in xq_map.keys():
        print reg
    sys.exit()

with open('data.csv', 'r') as f:
    for line in f:
        cols = line.split(',')
        if not cols[0].startswith('https'):
            continue
        xq = cols[1].strip('"')
        if xq not in xq_map[region]:
            continue
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
