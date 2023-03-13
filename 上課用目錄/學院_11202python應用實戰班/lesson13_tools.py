class Person():
    def __init__(self,name,age,isMan) -> None:
        super().__init__()
        self.__name__ = name
        self.__age__ = age
        self.__isMan__ = isMan
    
    @property
    def name(self):
        return self.__name__
    
    @property
    def age(self):
        return self.__age__
    
    @property
    def sex(self):
        if self.__isMan__:
            return "男"
        else:
            return "女"

    #override(覆寫)父類別的method
    def __repr__(self) -> str:
        own = super().__repr__()
        return f"我是Person類別建立出來的實體\n{own}"