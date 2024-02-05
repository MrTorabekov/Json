import json


my_info = {
    "name": "PDPschool",
    "email": "PDPschool@gmail.com",
    "url": "http://PDPschool.com",
    "username": "@PDPschool",
    "age": "6 oy",
    "ful_name ": {
        "first_name": "PDP school",
        "last_name": "PDP Universitet",
    }
}

with open("pdpschool.json","w") as file_json:
    json.dump(my_info, file_json)