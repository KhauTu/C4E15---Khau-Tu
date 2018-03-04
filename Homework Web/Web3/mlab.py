import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds153958.mlab.com:53958/service_web3

host = "ds153958.mlab.com" # Địa chỉ nhà
port = 53958
db_name = "service_web3"
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
