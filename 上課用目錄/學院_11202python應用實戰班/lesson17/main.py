
from tools import Taiwan_AQI

def main():
    try:
        aqi_list = Taiwan_AQI.download_aqi()
    except Exception as err:
        print(str(err))
        return
    
    for item in aqi_list:
        print(item)
    
    

if __name__ == "__main__":
    main()