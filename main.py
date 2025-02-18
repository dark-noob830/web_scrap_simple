import requests
from fake_useragent import UserAgent


ua = UserAgent()
url = 'https://bama.ir/'
response = requests.get(url,headers={"User-Agent":ua.random})

print(response.status_code)