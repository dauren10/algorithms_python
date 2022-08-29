a = [1,2,3,4,6,7,2,3,4,6,7]
count =[0] * 8
for number in a:
    count[number]+=1
for i in range(len(count)):
    if count[i] > 0:
        print((str(i) + ' ') * count[i],end='')

print('end')
s = 'abbczjfglskspsflasd;sg 6522 ()$#'
letters = [0] * (len(s) +1)

for i in s.lower():
    if i>='a' and i<='z':
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(len(s)+1):
    print(chr(i+97),letters[i])