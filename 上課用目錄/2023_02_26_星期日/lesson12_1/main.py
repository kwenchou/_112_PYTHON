import tools
from tools import Person

def main() -> None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1 = Person()
    print(type(p1))
    p2 = Person()
    print(type(p2))


if __name__ == "__main__":    
    main()