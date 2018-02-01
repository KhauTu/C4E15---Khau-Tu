from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customer = db['customers']
# post = db['posts']

customer_list = customer.find()
# 1. Count the number of customers group by refs
e = 0
w = 0
a = 0

for cus in customer_list:
    # print(cus['ref'])
    if cus['ref'] == 'events':
        e += 1
    elif cus['ref'] == 'wom':
        w += 1
    else:
        a += 1
print(e, "events")
print(w, 'wom')
print(a, 'ads')

# 2. draw a pie chart showing how much percentage of each reference
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

# a. Prepare data
labels = ['events', 'wom', 'ads']
values = [e, w, a]
colors = ['red', 'gold', 'green']
explode = [0, 0.1, 0]

# b. Plot
pyplot.pie(values, labels = labels, colors = colors, explode = explode, shadow = True)
pyplot.axis('equal')

# c. Show
pyplot.show()
