way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
f = open(way, 'w')
for _ in range(1):
    a = -1
    b = int(0)
    c = int(0)
    BPM = int(input("请输入歌曲BPM(只能填数字否则报错):"))#useless
    a1 = int(input("请输入歌曲总毫秒数(只能填数字否则报错):"))
    section = BPM*a1/240#useless
    b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
    b1 = b1-1
    note = str(input("请输入使用的箭头:"))
    num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
    list1 = [","]
    a1 = a1-num1 #                     玩家角色                               敌方箭头数                       我方箭头数
    print("{",'"',"song",'"',":{",'"',"player1",'"',":",'"',"bf",'"',",",'"',"keyCount",'"',":","4",",",'"',"playerKeyCount",'"',":","4",",",'"',"notes",'"',":[{",'"'"sectionNotes",'"',":[",sep="",end="", file=f)
    while a <= a1:
        a = int(a + num1)
        if a1-a <= num1 and a+num1 >= a1:
            print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
            print(' '.join(list1), sep="", end="", file=f)
            list1 = [""]
            if b <= b1:
                b = int(b + 1)
            else:
                b = int(0)
        else:
            print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
            if b <= b1:
                b = int(b + 1)
            else:
                b = int(0)
    print("]",",",'"',"lengthInSteps",'"',":","16",","'"',"typeOfSection",'"',":","0",",",'"',"mustHitSection",'"',":","true",",",'"',"bpm",'"',":","0.1}]",",",'"',"player2",'"',":",'"',"bf",'"',",",'"',"chartOffset",'"',":","0",",",'"',"modchartPath",'"',":",'"','"',",",'"',"mania",'"',":null",",",'"',"modchartingTools",'"',":","false",",",'"',"endCutscene",'"',":",'"','"',",",'"',"song",'"',":",'"',"test",'"',",",'"',"validScore",'"',":","false",",",'"',"speed",'"',":","3",",",'"',"sectionLengths",'"',":","[]",",",'"',"ui_Skin",'"',":",'"',"default",'"',",",'"',"events",'"',":","[]",",",'"',"cutscene",'"',":",'"','"',",",'"',"timescale",'"',":[4,4],",'"',"needsVoices",'"',":true,",'"',"stage",'"',":",'"',"stage",'"',",",'"',"sections",'"',":0,",'"',"bpm",'"',":",BPM,",",'"',"gf",'"',":",'"',"gf",'"',"}}","'",sep="",end="", file=f)
f.close()#                                                                                 必按回合                              此回合bpm                           敌方角色                                                                 modchart                               mania                                                                                                        歌名                                                                        速度                                                              箭头皮肤                                     事件                                                                                            需要voices                      场景                                                             bpm                   GF
print("输出完成")
