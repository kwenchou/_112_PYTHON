'''
1. 題目說明:
請開啟PYD306.py檔案，依下列題意進行作答，依輸入值計算n!的值，使輸出值符合題意要求。作答完成請另存新檔為PYA306.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
計算n!的值

輸入輸出範例
範例輸入
15
範例輸出
1307674368000
'''

n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)