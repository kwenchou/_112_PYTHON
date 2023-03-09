#請輸入本期大樂透電腦選號的組數:10
import lottery


for n in range(int(input("請輸入本期大樂透電腦選號的組數:"))):
    lottery.lottery_poll()
    print(f"您將中大獎的大樂透電腦選號第{n+1}組:{lottery.lottery_poll()[:6]}&特別號為:{lottery.lottery_poll()[-1:]}")
print()
print("!!!!!!!!!!!!!!!祝您中大獎!!!!!!!!!!!!!!!")