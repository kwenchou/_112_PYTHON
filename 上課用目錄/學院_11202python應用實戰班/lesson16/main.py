
from tools import Taiwan_AQI

def main():
    try:
        Taiwan_AQI.download_aqi()
    except Exception as err:
        print(str(err))
        return
    
    

if __name__ == "__main__":
    main()