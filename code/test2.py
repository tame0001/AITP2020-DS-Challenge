import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import re
import statistics

DATABASE = '/home/train59/AITP2020-DS-Challenge/data/TREE.db'

engine = db.create_engine('sqlite:////home/train59/AITP2020-DS-Challenge/data/TREE.db')
connection = engine.connect()
metadata = db.MetaData()

plot = db.Table('PLOT', metadata, autoload=True, autoload_with=engine)
species = db.Table('SPECIES', metadata, autoload=True, autoload_with=engine)
tree = db.Table('TREE', metadata, autoload=True, autoload_with=engine)


query = db.select([species])
ResultProxy = connection.execute(query)
results = ResultProxy.fetchall()

species_list = []
for result in results:
    if result.SPCD not in species_list:
        species_list.append(result.SPCD)

# print(species_list)

file_path = '/home/train59/AITP2020-DS-Challenge/outputs/'

fh = open(f'/home/train59/AITP2020-DS-Challenge/outputs/hieght.txt', 'w')
fd = open(f'/home/train59/AITP2020-DS-Challenge/outputs/diameter.txt', 'w')

re_pattern = r'(.*):(.*):(.*):(.*):(.*):(.*):(.*):(.*)'

# spcd = 896
for spcd in species_list:
    data_list = []
    try:
        with open(f'/home/train59/AITP2020-DS-Challenge/data/{spcd}.txt') as fd: 
            lines = fd.readlines()
            for line in lines:
                results = re.findall(re_pattern, line.strip())
                data = {
                    'INVYR': results[0][0],
                    'STATECD': results[0][1],
                    'PLOT': results[0][2],
                    'HT': results[0][3],
                    'ACTUALHT': results[0][4],
                    'STATUSCD': results[0][5],
                    'DIA': results[0][6],
                    'HTCD': results[0][7],
                    
                }
                data_list.append(data)

        hieght_list = []
        dia_list = []
        max_hieght = 0
        max_dia = 0
        max_hieght_year = 0
        max_dia_year = 0
        for data in data_list:
            if int(data['STATUSCD']) == 1:
                try:
                    hieght_list.append(float(data['HT']))
                except:
                    pass
                try:
                    dia_list.append(float(data['DIA']))
                except:
                    pass
                if float(data['HT']) > max_hieght:
                    max_hieght = float(data['HT'])
                    max_hieght_year = data['INVYR']

                if float(data['DIA']) > max_dia:
                    max_dia = float(data['DIA'])
                    max_dia_year = data['INVYR']

        # print(hieght_list)
        # print(statistics.mean(hieght_list))

        # print(max_hieght)
        # print(max_hieght_year)


        # for result in results:    
        fh.write(f'{spcd},{max_hieght_year},{round(max_hieght, 2)},{round(statistics.mean(hieght_list), 2)},{round(statistics.stdev(hieght_list), 2)},{round(statistics.median(hieght_list), 2)}\n')
        fd.write(f'{spcd},{max_dia_year},{round(max_dia, 2)},{round(statistics.mean(dia_list), 2)},{round(statistics.stdev(dia_list), 2)},{round(statistics.median(dia_list), 2)}\n')
    except:
        pass

fh.close()
fd.close()