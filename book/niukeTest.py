#x 房租
#f 已经拥有的水果个数
#d 牛牛当前拥有的钱
#p 每个水果的价格
def yongGanNiuNiu(x,f,d,p):
    day = 0
    while f>0:
        d = d - x
        day = day + 1
        f = f -1
    while d>=0:
        day = day + 1
        d = d - (x + p)
    return day-1

if __name__ == "__main__":
    print(yongGanNiuNiu(3,5,100,10))

