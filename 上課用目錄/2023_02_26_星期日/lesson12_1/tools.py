import random
PI = 3.1415962
NAME = "我是tools內的常數Name"

def get_weather() -> str:
    return random.choice(['晴天','陰天','雨天','大太陽'])