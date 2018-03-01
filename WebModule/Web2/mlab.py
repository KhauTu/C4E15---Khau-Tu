import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds249818.mlab.com:49818/muadong_khonglanh

host = "ds249818.mlab.com" # Địa chỉ nhà
port = 49818
db_name = "muadong_khonglanh"
user_name = "KhauTuD"
password = "Tahy22495"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
