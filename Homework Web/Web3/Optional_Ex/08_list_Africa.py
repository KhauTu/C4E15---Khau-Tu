from pymongo import *
import mlab
from models.river import River
mlab.connect()

all_africa = River.objects()

for k, v in enumerate(all_africa):
    if v['continent'] == 'Africa':
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
# africa_list = all_river.find({"continent": "Africa"})
# for africa in africa_list:
#     print(africa["name"])
