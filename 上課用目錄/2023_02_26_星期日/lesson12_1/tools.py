import random
PI = 3.1415962
NAME = "我是tools內的常數Name"

def get_weather() -> str:
    return random.choice(['晴天','陰天','雨天','大太陽'])

class Person:
    def __init__(self):
        #實體的attribute
        self.name = "徐國堂"
        self.age = 40
