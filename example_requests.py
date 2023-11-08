import requests
import json

url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srprop=snippet&format=json&origin=*&utf8=&srsearch=juegos olimpicos"

payload = ""
headers = {
  'Cookie': 'GeoIP=CO:DC:Bogot__:4.61:-74.08:v4; WMF-Last-Access-Global=01-Nov-2023; NetworkProbeLimit=0.001; WMF-Last-Access=01-Nov-2023'
}

response = requests.request("GET", url, headers=headers, data=payload)

response_dict = json.loads(response.text)

print(response_dict)

# Logica deseada dependiendo de la aplicación

info_list = response_dict["query"]["search"]


for index, info in enumerate(info_list):
    print("Info: ", index)
    print(info["title"])

print()


