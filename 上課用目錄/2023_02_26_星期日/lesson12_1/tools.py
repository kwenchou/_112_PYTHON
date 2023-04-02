import random
PI = 3.1415962
NAME = "我是tools內的常數Name"

def get_weather() -> str:
    return random.choice(['晴天','陰天','雨天','大太陽'])

def get_person(name, age, score):
    return Person(name,age,score=score)

class Person:
    def __init__(self,name,age,score=0):        
        self.__name = name
        self.__age = age
        #實體的attribute,可被取出,也可以被寫入
        self.score = score

    #實體的property,可以讓實體取出
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age


    #實體方法method()
    def print_detail(self) -> None:
        print(f"name:{self.__name}")
        print(f"age:{self.__age}")
        print(f"score:{self.score}")
