import time
#建立一個執行緒要執行的function
def countdown(n):
    while n > 0:
        print('倒數計時:',n)
        n -= 1
        time.sleep(5)


#建立和啟動執行緒
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

#由主執行緒執行以下程式碼, 並使用is_alive()檢查是否次執行緒還在執行
while t.is_alive():
    print('still running')
    time.sleep(1)
else:
    print('Completed')