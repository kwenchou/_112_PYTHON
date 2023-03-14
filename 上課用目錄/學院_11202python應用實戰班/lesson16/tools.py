import requests

API_KEY = "b8416fe0-3673-4eac-be88-7ac4bb9fce06"

def download_aqi() -> list:
    response=requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')
    print(response.text)