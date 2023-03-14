from tools import add
from tools import Tool

def main() -> None:
    print(add(4.5, 9.7))
    print(Tool.add(4.5, 9.7))

if __name__ == '__main__':
    main()