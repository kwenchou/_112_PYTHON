import tools
from tools import Person

def main() -> None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1 = Person("徐國堂",40)
    p1.score = 78   
    print(p1.name)
    print(p1.age)
    print(p1.score)

    p2 = Person("alice",24)
    p2.score = 65
    print(p2.name)
    print(p2.age)
    print(p2.score)
    


if __name__ == "__main__":    
    main()