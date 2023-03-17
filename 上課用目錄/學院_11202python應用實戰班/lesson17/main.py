
from tools import Taiwan_AQI

def get_best(dataList) -> list:
    sorted_data = sorted(dataList,key=lambda a:a.aqi,reverse=True)
    for item in sorted_data:
        print(item)

def get_bad(dataList) -> list:
    pass

def print_site_level() -> None:
    pass

def main():
    try:
        aqi_list = Taiwan_AQI.download_aqi()
    except Exception as err:
        print(str(err))
        return
    
    get_best(aqi_list)
    

if __name__ == "__main__":
    main()