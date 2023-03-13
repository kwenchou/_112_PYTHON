class Person():
    def __init__(self,name,age,isMan) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.isMan = isMan

    #override(覆寫)父類別的method
    def __repr__(self) -> str:
        own = super().__repr__()
        return f"我是Person類別建立出來的實體\n{own}"