import mlab
from models.service import Service

mlab.connect()
#
# all_service = Service.objects()
#
# first_service = all_service[0]
#
# print(first_service.name) # first_service['name']

id_to_find = '5a955a45c0e89627f0dd2303'

service = Service.objects().with_id(id_to_find)

print(service.to_mongo())

if service is not None:
    # service.delete()
    service.update(set__yob = 1998)
    service.reload() # service = Service.objects().with_id(id_to_find)
    print(service.to_mongo())
else:
    print('Not found!')

# Linda.delete()
