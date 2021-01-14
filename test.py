import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Python API Video", "views": 2500, "likes": 10,}, 
         {"name": "Python train", "views": 85000,"likes": 12334},
         {"name": "Python API Video 2", "views": 99500, "likes": 15200}]

for i in range (0, len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/2")
print(response)