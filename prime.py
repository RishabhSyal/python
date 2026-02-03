a = int(input("Enter value till which you want to find prime numbers: "))
flag = True
final_list = list()
final_list.append(2)
for i in range (3,a+1):
    for j in range (2,i):
        if i%j==0:
            flag = False
            break
    if flag == True:
        final_list.append(i)
    i+=1
    flag = True
print (final_list)
