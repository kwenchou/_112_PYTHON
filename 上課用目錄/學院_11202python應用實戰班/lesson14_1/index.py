from tools import BMI

def main() -> None:
    b1 = BMI("robert",age=35,isMan=True)
    print(b1.info())

    b2 = BMI("alice",isMan=False)
    print(b2.info())


if __name__ == "__main__":
    main()