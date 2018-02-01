import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

# 1. Prepare data
labels = ['Android', 'iOS', 'Web']
values = [300, 400, 300]
colors = ['red', 'gold', 'green']
explode = [0, 0.1, 0]

# 2. Plot
pyplot.pie(values, labels = labels, colors = colors, explode = explode, shadow = True)
pyplot.axis('equal')

# 3. Show
pyplot.show()
