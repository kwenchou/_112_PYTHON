#請輸入本期大樂透電腦選號的組數:10
import tools


for n in range(int(input("請輸入本期大樂透電腦選號的組數:"))):
    values = tools.lottery_poll()
    print(f"您將中大獎的大樂透電腦選號第{n+1}組:{values[:6]}&特別號為:{values[-1:]}")
print()
print("!!!!!!!!!!!!!!!祝您中大獎!!!!!!!!!!!!!!!")