import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

DATABASE = '/home/train59/AITP2020-DS-Challenge/data/TREE.db'

engine = db.create_engine('sqlite:////home/train59/AITP2020-DS-Challenge/data/TREE.db')
connection = engine.connect()
metadata = db.MetaData()

plot = db.Table('PLOT', metadata, autoload=True, autoload_with=engine)
species = db.Table('SPECIES', metadata, autoload=True, autoload_with=engine)
tree = db.Table('TREE', metadata, autoload=True, autoload_with=engine)

# query = db.select([plot])
# ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()

# print(census.columns.keys())

# print(len(ResultSet))

query = db.select([species])
ResultProxy = connection.execute(query)
results = ResultProxy.fetchall()

species_list = []
for result in results:
    if result.SPCD not in species_list:
        species_list.append(result.SPCD)

for pscd in species_list:
    query = db.select([tree]).where(tree.columns.SPCD == pscd)
    ResultProxy = connection.execute(query)
    # results = ResultProxy.fetchmany(50)
    results = ResultProxy.fetchall()

    f = open(f'/home/train59/AITP2020-DS-Challenge/data/{pscd}.txt', 'w')
    for result in results:    
        f.write(f'{result.INVYR}:{result.STATECD}:{result.PLOT}:{result.HT}:{result.ACTUALHT}:{result.STATUSCD}:{result.DIA}:{result.HTCD}\n')
    f.close()
# query = db.select([tree])
# query = db.select([tree]).where(tree.columns.STATECD == 1)
# ResultProxy = connection.execute(query)
# results = ResultProxy.fetchmany(500)
# results = ResultProxy.fetchall()

# species_list = []
# print(len(results))
# for result in results:
#     if result.SPCD not in species_list:
#         species_list.append(result.SPCD)


# print(species_list)
# print(len(species_list))
