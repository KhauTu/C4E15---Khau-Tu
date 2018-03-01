import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151508.mlab.com:51508/warmwinter

host = "ds151508.mlab.com" # Địa chỉ nhà
port = 51508
db_name = "warmwinter"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
