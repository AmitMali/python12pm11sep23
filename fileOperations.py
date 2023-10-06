# myfile=open("testfile.txt",'a')
# myfile.write("hum kuch alga likhate hai \n")
# myfile.close()
# myfile=open("testfile.txt",'r')
# print(myfile.readlines())
# myfile.close()

# with open('testfile.txt','r') as myfile:
#     print(myfile.read())

# with open('users.csv','a') as usersFile:
#     usersFile.write("Sushil Khatri,9595949345,male,sushil@gmail.com\n")

import requests as req
import json
responce=req.get(f"https://jsonplaceholder.typicode.com/users/")
result=json.loads(responce.text)
with open("users.csv",'a') as usersFile:
    usersFile.write(f"id,name,username,email\n")
    for user in result:
        usersFile.write(f"{user['id']},{user['name']},{user['username']},{user['email']}\n")
