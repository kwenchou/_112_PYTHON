import requests

def main():
    response=requests.get('https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=xxxxxxxxxx&limit=1000&sort=ImportDate desc&format=CSV')
    print(response.text)

if __name__ == "__main__":
    main()