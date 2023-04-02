import random
PI = 3.1415962
NAME = "我是tools內的常數Name"

def get_weather() -> str:
    return random.choice(['晴天','陰天','雨天','大太陽'])

class Person:
    def __init__(self,name,age,score=0):
        #實體的attribute,可被取出,也可以被寫入
        self.name = name
        self.age = age
        self.score = score

    #實體方法
    def print_detail(self) -> None:
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"score:{self.score}")
