from tools import BMI,Student

def main() -> None:
    b1 = BMI("robert",h=170,w=76.6,age=35,isMan=True)
    print(b1.name)
    print(b1.bmi)

    s1 = Student("alice",chinese=67,math=78,english=67,isMan=False)
    print(f'總分:{s1.sum}')
    print(f'平均:{s1.average}')


if __name__ == "__main__":
    main()