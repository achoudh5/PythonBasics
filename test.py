import json

data = {
    "president": {
        "name":"zaphod",
        "species": "Betel"
    }
}

with open("data_file.json","w") as write_file:
    json.dump(data, write_file)

json_string= json.dumps(data)
print json_string

with open("data_file.json","r") as read_file:
    data1 =json.load(read_file)

data1=json.loads(data)
print data1