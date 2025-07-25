s="hello world"
i,length = len(s)-1,0
while s[i]== " ":
    i -= 1
while i>=0 and s[i] != " ":
    length +=1
    i -= 1
print(length)