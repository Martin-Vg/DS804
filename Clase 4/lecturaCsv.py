from sys import argv, exit
import csv
import re

if len(argv) < 3: # comprobacion de argumentos 
    exit("Missing arguments")

if not(re.match(r'.+\.csv$', argv[1])): # comprobacion de tipo de archivo
    print(argv[1])
    sys.exit("Fisrt argument must be a csv file")

i=0
with open(argv[1]) as csvfile: # abrimos archivo en la ruta de argumento [1]
    reader = csv.DictReader(csvfile)
    for row in reader:
        i+=1 
        try:
            print(row[argv[2]]) # comprobamos que exista la columna si no mandamos un mensaje
        except:
            sys.exit("Column not found")
with open(argv[1], 'a') as csvfile:
    writer = csv.writer(csvfile)# abrimos el documento como escritura para agregar texto al final
    writer.writerow([1] * i)

