test_numbers = int(input())
output = []
for i in range(test_numbers):
    ans = ""
    main_time = input()
    if (main_time[:2] != "12"): hour = main_time[:5]
    else: hour = "00" + main_time[2:5]
    friend_numbers = int(input())
    for j in range(friend_numbers):
        times = input()
        
        
        if (times[:2] != "12"): hour_1 = times[:5]
        else: hour_1 = "00" + times[2:5]
        if (times[9:11] != "12"): hour_2 = times[9:14]
        else: hour_2 = "00" + times[11:14]
        
        if ((main_time[6] == times[6]) and (main_time[6] != times[15]) and (hour >= hour_1)): ans += '1'
        elif ((main_time[6] == times[15]) and (main_time[6] != times[6]) and (hour <= hour_2)): ans += '1'
        elif ((main_time[6] == times[6]) and (main_time[6] == times[15]) and (hour >= hour_1) and (hour <= hour_2)): ans += '1'
        else: ans += '0'
    
    output.append(ans)

for out in output:
    print(out)