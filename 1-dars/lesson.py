import json


my_info = {
    "name": "Diyorbek",
    "email": "Diyorbek@gmail.com",
    "url": "http://diyorbek",
    "username": "@Torabekov",
    "age": 18,
    "ful_name ": {
        "first_name": "Diyorbek",
        "last_name": "Torabekov"
    }
}

data = json.dumps(my_info)
print(data)
print(type(data))