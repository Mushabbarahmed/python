#to know more aboutbthis module check in request modules in python(seach for http request for humans
import requests
#
# url="www.something.com"
# data={
#     "p1":4,
#     "p2":3
# }
# r=requests.post(url=url,data=data)
r=requests.get("https://developer.mozilla.org/en-US/docs/Web/HTTP/Status")
print(r)
print(r.status_code)#to check the response(there are many ways u can check about status you can go to google and seacrh n for status code