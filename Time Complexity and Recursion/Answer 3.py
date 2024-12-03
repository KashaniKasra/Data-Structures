inp = input()
max_size = 0
for i in range(len(inp)):
    ans = ""
    for char in inp[i:len(inp)+1]:
        if (char not in ans): 
            ans += char
            if (len(ans) > max_size): max_size = len(ans)
        else: break
print(max_size)