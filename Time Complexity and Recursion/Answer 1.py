my_str = input()

bit_dict = {}
bit_dict[0] = 1
for i in range(1, 1024):
    bit_dict[i] = 0
    
bit_num = 0
ans = 0
for c in my_str:
    bit_index = ord(c) - ord('a')
    bit_num = bit_num ^ (1 << bit_index)
    ans = ans + bit_dict[bit_num]
    
    for i in range(10):
        ans = ans + bit_dict[bit_num ^ (1 << i)]
        
    bit_dict[bit_num] += 1

print(ans)