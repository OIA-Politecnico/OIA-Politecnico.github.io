#!/usr/bin/env python3

import csv
import sys
from collections import defaultdict

data = open('temario.tsv', 'r')

temario = defaultdict(lambda: defaultdict(list))
for row in csv.DictReader(data, delimiter='\t'):
	cat = row['Categoria']
	subcat = row['Subcategoria']
	tema = row['Tema']

	temario[cat][subcat].append(tema)
	
print('#', 'Temario extendido')

for cat in temario:
	print('')
	print('##', cat)
	print('')

	for subcat in temario[cat]:

		if subcat != '':
			print('')
			print('###', subcat)
			print('')

		for tema in temario[cat][subcat]:
			print('-', tema)

