#讓使用者輸入梯形的上底、下底及高，程式會計算梯形的面積(上底加下底乘以高除以2)

top = eval(input('請輸入梯形的上底(公分):'))
bottom = eval(input('請輸入梯形的下底(公分):'))
height = eval(input('請輸入梯形的高(公分):'))
area = (top + bottom) * height / 2
print(f"梯形的面積:{area:.2f}平方公分")
