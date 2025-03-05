import requests
NAME = 'fox'
Key = "OraJs8wSoCxsuaSufdDG5A==geBlmOnQQKafik7c"
URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(NAME)

response = requests.get(URL, headers={'X-Api-Key': Key})
if response.status_code == requests.codes.ok:
    list_of_type = response.json()
else:
    print("Error:", response.status_code, response.text)
counter= 0
for type in list_of_type:
    print (type["name"], end =", ")
    counter += 1
print()
print(counter)