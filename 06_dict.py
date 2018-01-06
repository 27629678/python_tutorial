# dictionary

dir(dict)
# ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribut
# e__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__
# ', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromk
# eys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# , 'viewitems', 'viewkeys', 'viewvalues']

post = {"uid": 2204, "name": "hzyuxiaohua", "email": "yuxiaohua.apple@gmail.com"}

type(post)

# (type 'dict')

post["uid"] = 2204
post["name"] = "hzyuxiaohua"

# accessing dictionary item
print(post["id"])

if 'location' in post:
    print post["location"]
else:
    print "the post does not contain a location value."

try:
    print(post['location'])
except KeyError:
    print "the post does not contain a location value."

for k,v in post.items():
    print(k, "=", v)

# id = 2204
# name = "hzyuxiaohua"