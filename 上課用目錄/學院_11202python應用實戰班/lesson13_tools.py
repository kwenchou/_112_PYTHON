class Person():
    def __init__(self) -> None:
        super().__init__()
        self.name = "徐國堂"

    #override(覆寫)父類別的method
    def __repr__(self) -> str:
        own = super().__repr__()
        return f"我是Person類別建立出來的實體\n{own}"