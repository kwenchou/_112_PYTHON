class Person():
    def __init__(self,name,age=20,isMan=True) -> None:
        super().__init__()
        self.__name  =  name
        self.__age = age
        self.__isMan = isMan
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def sex(self):
        if self.__isMan:
            return "男"
        else:
            return "女"
        
    def info(self) -> str:
        message  = ""
        message += f"我的姓名是{self.name}\n"
        message += f"我的age={self.age}\n"
        message += f"我的性別是{self.sex}"
        return message

class BMI(Person):
    def __init__(self,n) -> None:
        super().__init__(n)