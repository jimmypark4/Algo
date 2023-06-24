N = int(input())
arr = list(map(int,input().split()))
set_arr = set(arr)
s =list(set_arr)
s.sort()
# print(s)

def binary_search(s, a):
    st,en = 0 ,len(s)-1
    while st <= en:
        mid = int( (st+en)/2 )
        # print(st,mid,en,s[mid],a)

        if s[mid] == a:
            return mid
        elif s[mid] > a:
            en = mid - 1
        elif s[mid] < a:
            st = mid + 1






for a in arr:
    print(binary_search(s,a),end="\n")
    # print()