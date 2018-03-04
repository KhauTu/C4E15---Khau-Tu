from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds151508.mlab.com:51508/warmwinter"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customer = db['customer']

cus_list = customer.find()
# id_list = []
# for c in cus_list:
#     id_list = id_list.append(c['_id'])
# id_found = []
# for i in id_list:
#     id_found = id_found.append(i['$oid'])
# print(id_found)
