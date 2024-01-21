import random
mode = int(input("请输入模式前的数字\n1.纯大粪2.随机箭头3.随机双压箭头4.随机3押箭头"))
if mode == 1:
    way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
    f = open(way, 'w')
    for _ in range(1):
        a = -1
        b = int(0)
        c = int(0)
        songname = input("请输入歌名:")
        BPM = int(input("请输入歌曲BPM(只能填数字否则报错):"))
        a1 = int(input("请输入歌曲总毫秒数(只能填数字否则报错):"))
        section = BPM * a1 / 240
        b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
        b1 = b1 - 1
        note = str(input("请输入使用的箭头:"))
        num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
        list1 = [","]
        a1 = a1 - num1  # 玩家角色                               敌方箭头数                       我方箭头数
        print("{", '"', "song", '"', ":{", '"', "player1", '"', ":", '"', "bf", '"', ",", '"', "keyCount", '"', ":", b1,
              ",", '"', "playerKeyCount", '"', ":", b1, ",", '"', "notes", '"', ":[{", '"'"sectionNotes", '"', ":[",
              sep="", end="", file=f)
        while a <= a1:
            a = int(a + num1)
            if a1 - a <= num1 and a + num1 >= a1:
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
        print("]", ",", '"', "lengthInSteps", '"', ":", "16", ","'"', "typeOfSection", '"', ":", "0", ",", '"',
              "mustHitSection", '"', ":", "true", ",", '"', "bpm", '"', ":", "0.1}]", ",", '"', "player2", '"', ":",
              '"', "bf", '"', ",", '"', "chartOffset", '"', ":", "0", ",", '"', "modchartPath", '"', ":", '"', '"', ",",
              '"', "mania", '"', ":null", ",", '"', "modchartingTools", '"', ":", "false", ",", '"', "endCutscene", '"',
              ":", '"', '"', ",", '"', "song", '"', ":", '"', songname, '"', ",", '"', "validScore", '"', ":", "false",
              ",", '"', "speed", '"', ":", "3", ",", '"', "sectionLengths", '"', ":", "[]", ",", '"', "ui_Skin", '"',
              ":", '"', "default", '"', ",", '"', "events", '"', ":", "[]", ",", '"', "cutscene", '"', ":", '"', '"',
              ",", '"', "timescale", '"', ":[4,4],", '"', "needsVoices", '"', ":true,", '"', "stage", '"', ":", '"',
              "stage", '"', ",", '"', "sections", '"', ":0,", '"', "bpm", '"', ":", BPM, ",", '"', "gf", '"', ":", '"',
              "gf", '"', "}}", "'", sep="", end="", file=f)
    f.close()
    print("输出完成")
else:
    if mode == 2:
        way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
        f = open(way, 'w')
        list1 = [","]
        for _ in range(1):
            a = -1
            b = int(0)
            c = int(0)
            open_3second_no_note = bool(input("是否启用前3秒无箭头(填True或False):"))
            if open_3second_no_note == "True":
                a = int(2999)
            else:
                a = -1
            BPM = int(input("请输入歌曲BPM(只能填数字否则报错):"))
            songname = input("请输入歌曲名:")
            a1 = int(input("请输入歌曲总秒数(只能填数字否则报错):"))
            a1 = a1 * 1000
            section = BPM * a1 / 240
            b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
            b1 = b1 - 1
            note = str(input("请输入使用的箭头:"))
            num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
            a1 = a1 - num1  # 玩家角色                               敌方箭头数                       我方箭头数
            print("{", '"', "song", '"', ":{", '"', "player1", '"', ":", '"', "bf", '"', ",", '"', "keyCount", '"', ":",
                  b1+1, ",", '"', "playerKeyCount", '"', ":", b1+1, ",", '"', "notes", '"', ":[{", '"'"sectionNotes", '"',
                  ":[", sep="", end="", file=f)
            while a <= a1:
                a = int(a + num1)
                if a1 - a <= num1 and a + num1 >= a1:
                    b = random.randint(0, b1)
                    print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                    print(' '.join(list1), sep="", end="", file=f)
                    list1 = [""]
                else:
                    b = random.randint(0, b1)
                    print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
            print("]", ",", '"', "lengthInSteps", '"', ":", "16", ","'"', "typeOfSection", '"', ":", "0", ",", '"',
                  "mustHitSection", '"', ":", "true", ",", '"', "bpm", '"', ":", "0.1}]", ",", '"', "player2", '"', ":",
                  '"', "bf", '"', ",", '"', "chartOffset", '"', ":", "0", ",", '"', "modchartPath", '"', ":", '"', '"',
                  ",", '"', "mania", '"', ":null", ",", '"', "modchartingTools", '"', ":", "false", ",", '"',
                  "endCutscene", '"', ":", '"', '"', ",", '"', "song", '"', ":", '"', songname, '"', ",", '"',
                  "validScore", '"', ":", "false", ",", '"', "speed", '"', ":", "3", ",", '"', "sectionLengths", '"',
                  ":", "[]", ",", '"', "ui_Skin", '"', ":", '"', "default", '"', ",", '"', "events", '"', ":", "[]",
                  ",", '"', "cutscene", '"', ":", '"', '"', ",", '"', "timescale", '"', ":[4,4],", '"', "needsVoices",
                  '"', ":true,", '"', "stage", '"', ":", '"', "stage", '"', ",", '"', "sections", '"', ":0,", '"',
                  "bpm", '"', ":", BPM, ",", '"', "gf", '"', ":", '"', "gf", '"', "}}", "'", sep="", end="", file=f)
        f.close()
        print("输出完成")
    else:
        if mode == 3:
            way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
            f = open(way, 'w')
            list1 = [","]
            for _ in range(1):
                a = -1
                b = int(0)
                c = int(0)
                open_3second_no_note = bool(input("是否启用前3秒无箭头(填True或False):"))
                if open_3second_no_note == "True":
                    a = int(2999)
                else:
                    a = -1
                BPM = int(input("请输入歌曲BPM(只能填数字否则报错):"))
                songname = input("请输入歌曲名:")
                a1 = int(input("请输入歌曲总秒数(只能填数字否则报错):"))
                a1 = a1 * 1000
                section = BPM * a1 / 240
                b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
                b1 = b1 - 1
                note = str(input("请输入使用的箭头:"))
                num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
                a1 = a1 - num1  # 玩家角色                               敌方箭头数                       我方箭头数
                print("{", '"', "song", '"', ":{", '"', "player1", '"', ":", '"', "bf", '"', ",", '"', "keyCount", '"',
                      ":", b1+1, ",", '"', "playerKeyCount", '"', ":", b1+1, ",", '"', "notes", '"', ":[{",
                      '"'"sectionNotes", '"', ":[", sep="", end="", file=f)
                while a <= a1:
                    a = int(a + num1)
                    if a1 - a <= num1 and a + num1 >= a1:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                        print(' '.join(list1), sep="", end="", file=f)
                        list1 = [""]
                    else:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                print("]", ",", '"', "lengthInSteps", '"', ":", "16", ","'"', "typeOfSection", '"', ":", "0", ",", '"',
                      "mustHitSection", '"', ":", "true", ",", '"', "bpm", '"', ":", "0.1}]", ",", '"', "player2", '"',
                      ":", '"', "bf", '"', ",", '"', "chartOffset", '"', ":", "0", ",", '"', "modchartPath", '"', ":",
                      '"', '"', ",", '"', "mania", '"', ":null", ",", '"', "modchartingTools", '"', ":", "false", ",",
                      '"', "endCutscene", '"', ":", '"', '"', ",", '"', "song", '"', ":", '"', songname, '"', ",", '"',
                      "validScore", '"', ":", "false", ",", '"', "speed", '"', ":", "3", ",", '"', "sectionLengths",
                      '"', ":", "[]", ",", '"', "ui_Skin", '"', ":", '"', "default", '"', ",", '"', "events", '"', ":",
                      "[]", ",", '"', "cutscene", '"', ":", '"', '"', ",", '"', "timescale", '"', ":[4,4],", '"',
                      "needsVoices", '"', ":true,", '"', "stage", '"', ":", '"', "stage", '"', ",", '"', "sections",
                      '"', ":0,", '"', "bpm", '"', ":", BPM, ",", '"', "gf", '"', ":", '"', "gf", '"', "}}", "'",
                      sep="", end="", file=f)
            f.close()
            print("输出完成")
        else:
            way = input("请输入你要输出的路径(比如D:/test.json,不能使用\\):")
            f = open(way, 'w')
            list1 = [","]
            for _ in range(1):
                a = -1
                b = int(0)
                c = int(0)
                open_3second_no_note = input("是否启用前3秒无箭头(填yes或no):")
                if open_3second_no_note == "yes":
                    a = int(2999)
                else:
                    a = int(-1)
                BPM = int(input("请输入歌曲BPM(只能填数字否则报错):"))
                songname = input("请输入歌曲名:")
                a1 = int(input("请输入歌曲总秒数(只能填数字否则报错):"))
                a1 = a1 * 1000
                section = BPM * a1 / 240
                b1 = int(input("请输入歌曲总key数(只能填数字否则报错):"))
                b1 = b1 - 1
                note = str(input("请输入使用的箭头:"))
                speed = input("请输入歌曲速度:")
                num1 = int(input("请输入每个箭头间隔多少毫秒(只能填数字否则报错):"))
                a1 = a1 - num1  # 玩家角色                               敌方箭头数                       我方箭头数
                print("{", '"', "song", '"', ":{", '"', "player1", '"', ":", '"', "bf", '"', ",", '"', "keyCount", '"',
                      ":", b1+1, ",", '"', "playerKeyCount", '"', ":", b1+1, ",", '"', "notes", '"', ":[{",
                      '"'"sectionNotes", '"', ":[", sep="", end="", file=f)
                while a <= a1:
                    a = int(a + num1)
                    if a1 - a <= num1 and a + num1 >= a1:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b3 = b
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b3 or b == b2:
                                b = random.randint(0, b1)
                            if b != b3 and b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", sep="", end="", file=f)
                        print(' '.join(list1), sep="", end="", file=f)
                        list1 = [""]
                    else:
                        b = random.randint(0, b1)
                        b2 = b
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b2:
                                b = random.randint(0, b1)
                            if b != b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                        b3 = b
                        b = random.randint(0, b1)
                        for i in range(0, -1, -1):
                            if b == b3 or b == b2:
                                b = random.randint(0, b1)
                            if b == b3 and b == b2:
                                continue
                        print("[", a, ",", b, ",", "0", ",", "0", ","'"', note, '"', "]", ",", sep="", end="", file=f)
                print("]", ",", '"', "lengthInSteps", '"', ":", "16", ","'"', "typeOfSection", '"', ":", "0", ",", '"',
                      "mustHitSection", '"', ":", "true", ",", '"', "bpm", '"', ":", "0.1}]", ",", '"', "player2", '"',
                      ":", '"', "bf", '"', ",", '"', "chartOffset", '"', ":", "0", ",", '"', "modchartPath", '"', ":",
                      '"', '"', ",", '"', "mania", '"', ":null", ",", '"', "modchartingTools", '"', ":", "false", ",",
                      '"', "endCutscene", '"', ":", '"', '"', ",", '"', "song", '"', ":", '"', songname, '"', ",", '"',
                      "validScore", '"', ":", "false", ",", '"', "speed", '"', ":", speed, ",", '"', "sectionLengths",
                      '"', ":", "[]", ",", '"', "ui_Skin", '"', ":", '"', "default", '"', ",", '"', "events", '"', ":",
                      "[]", ",", '"', "cutscene", '"', ":", '"', '"', ",", '"', "timescale", '"', ":[4,4],", '"',
                      "needsVoices", '"', ":true,", '"', "stage", '"', ":", '"', "stage", '"', ",", '"', "sections",
                      '"', ":0,", '"', "bpm", '"', ":", BPM, ",", '"', "gf", '"', ":", '"', "gf", '"', "}}", "'",
                      sep="", end="", file=f)
            f.close()
            print("输出完成")