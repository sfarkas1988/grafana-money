import csv
from os import walk
import db

connection = db.connect()
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