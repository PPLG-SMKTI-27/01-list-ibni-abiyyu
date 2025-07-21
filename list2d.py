nilai=[[10,20,30],
       [40,50,60],
       [70,80,90]]
sum = 0
for i in range(len(nilai)):
    for j in range(len(nilai[i])):
        sum = sum + nilai[i][j]
    print(sum)
    sum = sum * 0