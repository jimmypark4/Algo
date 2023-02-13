S=input()
s_list=list(S)
#print(s_list)
alpha=[0]*27
for char in s_list:
    alpha[ord(char)-97]+=1
for i in range(26):
    print(alpha[i],end=" ")