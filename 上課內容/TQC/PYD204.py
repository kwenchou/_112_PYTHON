'''
1. 題目說明:
請開啟PYD204.py檔案，依下列題意進行作答，依輸入值進行算術運算，使輸出值符合題意要求。作答完成請另存新檔為PYA204.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。

3. 輸入輸出：
輸入說明
兩個整數a、b，及一個算術運算子 (+、-、*、/、//、%）

輸出說明
運算結果 (無須做格式化)

輸入輸出範例
範例輸入
30
20
*
範例輸出1
600
'''

a = int(input())
b = int(input())
opr = input()
ans = 0
if opr == '+':
    ans = a + b
elif opr == '-':
    ans = a - b
elif opr == '*':
    ans = a * b
elif opr == '/':
    ans = a / b
elif opr == '//':
    ans = a // b
elif opr == '%':
    ans = a % b

print(ans)

