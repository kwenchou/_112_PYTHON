import tools
from tools import Person

def main() -> None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1 = Person("徐國堂",40)
    print(f"p1的name:{p1.name}")
    print(f"p1的age:{p1.age}")
    print(f"p1的score:{p1.score}")
    p2 = Person("alice",24)
    print(f"p2的name:{p2.name}")
    print(f"p2的age:{p2.age}")
    print(f"p2的score:{p2.score}")


if __name__ == "__main__":    
    main()