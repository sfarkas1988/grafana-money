import csv
rows = csv.reader(open('Girokonto.csv', newline=''), delimiter=';')
for row in rows:
    print(', '.join(row))
