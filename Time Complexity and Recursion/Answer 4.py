def check_numbers(num1, num2, new_num):
    if (len(new_num) == 0):
        return True
    
    summ = num1 + num2
    for i in range(len(str(summ)) + 2):
        if (summ == int(new_num[ : i + 1])):
            return check_numbers(num2, summ, new_num[i + 1 : ])
    return False

my_num = input()
for i in range(len(my_num)):
    for j in range(i+1, len(my_num)):
        
        if (my_num[ : i + 1][0] == '0' or my_num[i + 1 : j + 1][0] == '0'):
            continue
        
        num1 = int(my_num[ : i + 1])
        num2 = int(my_num[i + 1 : j + 1])
        
        if(len(my_num[j + 1 : ]) > 0):
            if (check_numbers(num1, num2, my_num[j + 1 : ])):
                print("YES")
                exit()
print("NO")