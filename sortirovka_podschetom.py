a = [1,2,3,4,6,7,2,3,4,6,7]
count =[0] * 8
for number in a:
    count[number]+=1
for i in range(len(count)):
    if count[i] > 0:
        print((str(i) + ' ') * count[i],end='')
