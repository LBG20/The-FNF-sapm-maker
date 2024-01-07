way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
f = open(way, 'w')
a = -1
b = int(0)
a1 = int(input("请输入歌曲总毫秒数(只能填数字否则报错):"))
b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
b1 = b1 - 1
note = str(input("请输入使用的箭头:"))
num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
list1 = [","]
while a <= a1:
    a = int(a + num1)
    if a1 - a <= num1 and a + num1 >= a1:
        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
        print(' '.join(list1), sep="", end="", file=f)
        list1 = [""]
        if b <= 3:
            b = int(b + 1)
        else:
            b = int(0)
    else:
        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
        if b <= 3:
            b = int(b + 1)
        else:
            b = int(0)
f.close()
print("输出完成")