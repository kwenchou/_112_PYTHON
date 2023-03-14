ONE = 1
TWO = 2
THREE  = 3
FOUR = 4
FIVE = 5

def add(a,b) -> float:
    return a + b

class Tool(object):
    ONE = 1
    TWO = 2
    THREE  = 3
    FOUR = 4
    FIVE = 5

    @staticmethod
    def add(a,b) -> float:
        return a+b
    
    @classmethod
    def exclaim(cls)  -> None:
        print(cls.ONE)
        print(cls.TWO)
        print(cls.THREE)
        print(cls.FOUR)
        print(cls.FIVE)
