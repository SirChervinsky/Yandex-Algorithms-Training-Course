troom, tcond = map(int, input().split())
mode = input()
if mode == 'auto':
    print(tcond)
if mode == 'fan':
    print(troom)
if mode == 'freeze':
    if troom>tcond:
        print(tcond)
    else:
        print(troom)
if mode =='heat':
    if troom<tcond:
        print(tcond)
    else:
        print(troom)
