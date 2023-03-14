

class Taiwan_AQI():    
    API_KEY = "b8416fe0-3673-4eac-be88-7ac4bb9fce06"
    @classmethod
    def download_aqi(cls):
        import requests
        response=requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')
        
        print(response.text)