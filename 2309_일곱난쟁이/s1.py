import sys
sys.stdin = open('input.txt','r')

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()
iif = 0
ssum = sum(dwarf)
no1 = -1
no2 = -1
for i in range(0, 8):
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == ssum -100:
            iif = 1
            no1 = dwarf[i]
            no2 = dwarf[j]
            break
    if iif ==1 :
        break

for d in dwarf:
    if d != no1 and d != no2:
        print(d)

