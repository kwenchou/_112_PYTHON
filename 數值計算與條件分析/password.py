#!usr/bin/python3
'''
請依據 BMI 值分析他人的身體狀況。
- 讓使用者輸入密碼,如果輸入的密碼正確(1234), 要顯示「密碼正確!歡迎光臨!」。
- 如果不正確就顯示密碼錯誤訊息
'''

password = input('請輸入密碼:')
if password == "1234":
    print('密碼正確!歡迎光臨!')
else:
    print('密碼錯誤\n請重新輸入')