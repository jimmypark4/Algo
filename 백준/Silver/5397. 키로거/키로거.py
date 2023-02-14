import sys
input = sys.stdin.readline
N=int(input())
ans=[] #정답들이 들어감.
for i in range(N):
    testcase=list(input().rstrip())
    l_result=[]
    r_result=[]
    for char in testcase:
        if char == '<':
            if l_result !=[]:
                r_result.append(l_result.pop())
        elif char == ">":
            if r_result !=[]:
                l_result.append(r_result.pop())
        elif char == "-":
            if l_result !=[]:
                l_result.pop()
        else:
            l_result.append(char)
    # print(l_result,r_result[::-1])
    ans.append("".join ( l_result + r_result[::-1] )  )
print(*ans,sep="\n")