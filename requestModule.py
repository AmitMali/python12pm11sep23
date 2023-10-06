import requests as req
import json

uid=input("enter user id \n")
responce=req.get(f"https://jsonplaceholder.typicode.com/users/{uid}")
result=json.loads(responce.text)
# for user in result:
#     print(user['name'])
print(result)