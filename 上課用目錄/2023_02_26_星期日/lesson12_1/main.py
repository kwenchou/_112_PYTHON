import tools
from tools import Person

def main() -> None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1 = Person()
    print(f"p1的name{p1.name}")
    print(f"p1的age{p1.age}")
    p2 = Person()
    print(f"p2的name{p2.name}")
    print(f"p2的age{p2.age}")


if __name__ == "__main__":    
    main()