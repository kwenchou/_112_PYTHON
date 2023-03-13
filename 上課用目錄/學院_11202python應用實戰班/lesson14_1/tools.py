class Person():
    def __init__(self,name,age=20,isMan=True) -> None:
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