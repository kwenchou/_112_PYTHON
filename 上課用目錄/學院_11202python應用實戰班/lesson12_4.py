import requests

url = 'https://raw.githubusercontent.com/roberthsu2003/python/master/%E6%AA%94%E6%A1%88%E5%AD%98%E5%8F%96/%E5%80%8B%E8%82%A1%E6%97%A5%E6%88%90%E4%BA%A4%E8%B3%87%E8%A8%8A.csv'
response = requests.get(url)
print(response.text)