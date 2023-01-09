import requests as req

url = input("Enter the URL to be checked in the format https://www.examplewebsite.com or http://www.examplewebsite.com \n")

c = 1

while (c!=0):

    res =req.get(url)

    print(res)
    if(res.status_code == 200):
        print("Site is UP")
        c = 0
        pass

    else:
        print("Site is Down")
        c = 0
        pass
