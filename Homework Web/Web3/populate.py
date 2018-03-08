import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()
about1 = ['ngoan hiền', 'dễ thương', 'lễ phép', 'thông minh', 'cá tính',]
about2 = ['chăm chỉ', 'tốt bụng', 'xinh xắn', 'hòa đồng', 'nhiệt tình',]

# http://bit.ly/web3girl0
# http://bit.ly/web3girl1
# http://bit.ly/web3girl2
# http://bit.ly/web3girl3
# http://bit.ly/web3girl4
# http://bit.ly/web3girl5
# http://bit.ly/web3girl6
# http://bit.ly/web3girl7
# http://bit.ly/web3girl8


for i in range(10):
    print('Saving service', i + 1, '...')
    service = Service(name = fake.name(),
                    yob = randint(1995, 2000),
                    gender = 0,
                    height = randint(155, 165),
                    phone = fake.phone_number(),
                    address = fake.address(),
                    status = choice([True, False]),
                    image = 'http://bit.ly/web3girl{0}'.format(i),
                    desciption = choice(about1) + ', ' + choice(about2),
                    measurements = [90 + randint(-5, 5), 60 + randint(-3, 3), 90 + randint(-3, 3)])
    service.save()
    # link = 'http://bit.ly/web3girl{0}'.format(i)
    # desciption = choice(about1)+ ', ' + choice(about2)
    # print (desciption)
