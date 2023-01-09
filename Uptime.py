import requests as req
import time as t 

url = input("Enter the URL to be checked in the format https://www.examplewebsite.com or http://www.examplewebsite.com \n")

while True:
    res =req.get(url)
    
    if(res.status_code == 200):
        print("Site is UP")
        print(f"The Response code is {res.status_code}")
        pass

    else:
        print("Site is Down")
        print(f"The Response code is {res.status_code}")
        pass
    t.sleep(5)
