from pymongo import *
import mlab
from models.river import River
mlab.connect()

all_africa = River.objects()

for k, v in enumerate(all_africa):
    if v['continent'] == 'S. America' and v['length'] < 1000:
        print(v['name'])
        # print(v.to_mongo())
    else:
        pass
# Cách 2:
# from pymongo import MongoClient
#
# mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#
# river = MongoClient(mongo_uri)
#
# db = river.get_default_database()
#
# all_river = db['river']
#
# samerica_list = all_river.find({"continent": "S. America"})
# for samerica in samerica_list:
#     if samerica['length'] < 1000:
#         print(samerica["name"])
#     else:
#         pass
