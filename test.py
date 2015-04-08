__author__ = 'onurbaran'

from Map import Map

user = Map("user:12")
user.add("email", "baranonur@gmail.com")
user.add("name", "onur")
user.add("city", "ist")

print user
print len(user)

user.remove("city")
user.add("job", "developer")
print user.get("job")
print user
