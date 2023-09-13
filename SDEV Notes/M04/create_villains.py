import csv
import pandas

villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Lex', 'Luthor']
]

with open('villains.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

data = pandas.read_csv('villains.csv')
print(data)