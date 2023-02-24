import random
def playGame():
    print("==================猜數字遊戲==================\n")
    min = 1
    max = 100
    random_num = random.randint(min,max)
    used_num = 0
    print(random_num)
    while(True):
        keyin_value = int(input("猜數字範圍{0}~{1}:".format(min, max)))
        used_num += 1
        if(keyin_value >= min and keyin_value <= max):
            if keyin_value == random_num:
                print("賓果!猜對了,答案是:%d" % random_num)
                print(f"您猜了{used_num}次")
                break
            elif(keyin_value > random_num):
                print("再小一點")
                max = keyin_value - 1
                
            elif(keyin_value < random_num):
                print("再大一點")
                min = keyin_value + 1
                
            print(f"您已經猜了{used_num}次")
        else:
            print("超出範圍了!")
            continue


while(True):
    playGame()
    input_key = input("立即結束遊戲,請按「q」。按其它按鈕繼續遊戲!")
    if input_key == 'q':
        break
print("遊戲結束")