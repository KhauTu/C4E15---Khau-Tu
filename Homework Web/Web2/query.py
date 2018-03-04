import mlab
from models.customer import Customer

mlab.connect()
#
# all_service = Service.objects()
#
# first_service = all_service[0]
#
# print(first_service.name) # first_service['name']

id_to_find = '5a9772ffc0e89605287e4051'

Linda = Customer.objects.get(id = id_to_find)

print(Linda.to_mogo())
