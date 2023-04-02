import tools
from tools import Person

def main() -> None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1 = Person("徐國堂",40)
    p1.score = 78
    p1.print_detail()

    p2 = Person("alice",24)
    p2.score = 65
    p2.print_detail()


if __name__ == "__main__":    
    main()