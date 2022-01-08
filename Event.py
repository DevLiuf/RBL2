import DiceTumble

# 삼진, 그라운드 아웃, 플라이 아웃
# 볼넷, 안타, 2루타, 3루타, 홈런

#아웃카운트
OutCount = 0

#이닝
inning = 1

#공격 수비
offense = 0
defence = 0

#공격 아웃카운트
def OutCountTotal():
    if OutCount == 3:
        inning += 1
    return OutCount

#수비 아웃카운트
def OutCountPlus():
    global OutCount
    OutCount += 1
    if OutCount > 3:
        OutCount = 1
    if OutCount == 3:
        inning += 1
    return OutCount

def asd():
    Inning()
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

#공수교대
def OND():
    # global OutCount
    if OutCount == 3:
        print("====공수교대====")

def Inning():
    global inning
    print(f"{inning} 이닝")


def K():
    Inning()
    print("삼진")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()

def GO():
    Inning()
    print("그라운드 아웃")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()


def FO():
    Inning()
    print("플라이 아웃")
    OCP = OutCountPlus()
    print("아웃 카운트 ", OCP)
    OND()

def BB():
    Inning()
    print("볼넷")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def OneB():
    Inning()
    print("안타")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def DoubleB():
    # Inning()
    # print("2루타")
    # OCT = OutCountTotal()
    # print("아웃 카운트 ", OCT)
    print("2루타")
    asd()

def ThreeB():
    Inning()
    print("3루타")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)

def HR():
    Inning()
    print("홈런")
    OCT = OutCountTotal()
    print("아웃 카운트 ", OCT)


#===========================================================================================

def Result():
    D1 = DiceTumble.Dice1()
    D2 = DiceTumble.Dice2()
    result = DiceTumble.DicePlus()
    if result == 2:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        ThreeB()
    elif result == 3:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        BB()
    elif result == 4:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        DoubleB()
    elif result == 5:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        K()
    elif result == 6:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        GO()
    elif result == 7:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        OneB()
    elif result == 8:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        FO()
    elif result == 9:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        K()
    elif result == 10:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        DoubleB()
    elif result == 11:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        BB()
    elif result == 12:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1+D2)
        HR()




