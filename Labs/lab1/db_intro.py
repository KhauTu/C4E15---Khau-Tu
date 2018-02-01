from pymongo import MongoClient

mongo_uri = "mongodb://KhauTu:Tahy22495@ds113825.mlab.com:13825/c4e15-khautu"
# ds113825.mlab.com: Tên miền server
# 13825: cửa vào (port)
# c4e15-khautu: database

# 1. Open a connection to mlab
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Get collection
games = db['games'] # retrieve collection

game_list = games.find()

for game in game_list:
    print(game['description'])

# blog = db['blog']
#
# # 4. Create a new document
# new_game = {
#     'title': 'Witcher 3',
#     'description': 'Cool game'
# }
# new_blog ={
#     'Tieu de': 'Bong ban',
#     'Noi dung': 'Dau Team',
# }
# # 5. Put the created document into collection
# games.insert_one(new_game)
# blog.insert_one(new_blog)
