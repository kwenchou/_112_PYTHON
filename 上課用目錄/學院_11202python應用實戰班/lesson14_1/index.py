from tools import BMI

def main() -> None:
    b1 = BMI("robert",h=170,w=76.6,age=35,isMan=True)
    print(b1.name)
    print(b1.bmi)


if __name__ == "__main__":
    main()