import json
#javascript objject notation(json)
data='{"var1":"humaid","var2":"hashim"}'#to use json module for loads u have to use single qoute
print(data)
parsed=json.loads(data)
print(parsed["var1"])
# data2 ={
#     "channel_name":"humaid",
#     "car":["bmw","swift","ferari"],
#     "kitchen":("roti",540),
#     "isbad": False
# }
# jscon=json.dumps(data2)# this converts python into javascript
# print(jscon)
#there are many things in json module go through it 
