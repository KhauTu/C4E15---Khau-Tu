import mlab
from models.service import Service

mlab.connect()

all_service = Service.objects()

all_service.delete()
