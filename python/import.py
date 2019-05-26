import csv
import os

from os import listdir
from os.path import isfile, join

csv_path = "./csv"
files = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]


for f in files:
    file_path = csv_path +"/"+f
    file_extension = os.path.splitext(file_path)
    if file_extension[1] != ".csv":
        print(file_extension[1])
        continue

    print(file_path)
    rows = csv.reader(open(file_path, newline=''), delimiter=';')
    for row in rows:
        print(', '.join(row))

#from os import walk
#import db

#connection = db.connect()
#db.insert_sales()
#
# path = './csv'
# for (dirpath, dirnames, filenames) in walk(path):
#     for filename in filenames:
#         if filename.endswith('.csv'):
#             rows = csv.reader(open(path+'/'+filename, newline=''), delimiter=';')
#             for row in rows:
#                 print(row)
#             break

#Datum;Wertstellung;Kategorie;Name;Verwendungszweck;Konto;Bank;Betrag;Währung