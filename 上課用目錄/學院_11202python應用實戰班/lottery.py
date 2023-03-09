def lottery_poll():
    import random
    lottery = set()
    while (True):
        lottery.add(random.randint(1,50)) 
        if len(lottery) == 7:
            break
    all_lottery = list(lottery) #加list才有索引
    return all_lottery