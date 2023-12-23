#convert Python dict into JSON format, called serialization or enconding
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file)

#convert it back to Python, called D-serialization
person = json.loads(personJSON)
print(person)

with open('person.json', 'r') as file:
    print(json.load(file))

#convert a object to JSON
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userPy = User("Max", 17)

def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(userPy, default=encode_user)
print(userJSON)

#also works with "from json import JSONEncoder"
#using the same class User and userPy
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__:True}
        return JSONEncoder.default(self, obj)

userJSON = json.dumps(userPy, cls=UserEncoder)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user) 
print(user.name)
