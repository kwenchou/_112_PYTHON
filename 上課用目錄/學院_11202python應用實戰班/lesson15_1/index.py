from tools import add
from tools import Tool
from tools import ONE,TWO,THREE,FOUR,FIVE

def main() -> None:
    print(add(4.5, 9.7))
    print(Tool.add(4.5, 9.7))
    print(ONE)
    print(TWO)
    print(THREE)
    print(FOUR)
    print(FIVE)
    Tool.exclaim()

if __name__ == '__main__':
    main()