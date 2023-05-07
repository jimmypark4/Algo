n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(*arr,sep = '\n')

cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 or arr[i][j] == 3 or arr[i][j] == 4:
                cctv.append((arr[i][j],i,j))
        elif arr[i][j] == 2:
                cctv.append((arr[i][j],i,j))
        elif arr[i][j] == 5:
            cctv.append((arr[i][j],i,j))
# print(cctv)
#combination으로 simulation할 경우의 수 case 생성
case_num = len(cctv)
total_case_num = 4**case_num
dir_case = []
for i in range(total_case_num-1,-1,-1):
    temp_case = []
    temp = i
    for j in range(case_num):
        temp_case.append(temp%4)
        temp //=4
    dir_case.append(temp_case)
# print(dir_case)

dx = [0, 0, 1,-1]
dy = [1,-1, 0, 0]

def watch(x,y,direction,arr):
    nx = x +dx[direction]
    ny = y +dy[direction]
    while nx >= 0 and nx < m and ny >= 0 and ny < n and arr[ny][nx] != 6:#경계조건,벽 만날떄까지
        arr[ny][nx] = 8
        nx += dx[direction]
        ny += dy[direction]
    return arr
#simulation 수행
def simulation(type,x,y,direction,arr):
    if type == 1:
        arr = watch(x,y,direction,arr)

    elif type == 2:
        if direction == 0 or direction == 1:
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 1, arr)
        elif direction == 2 or direction == 3:
            arr = watch(x, y, 2, arr)
            arr = watch(x, y, 3, arr)

    elif type == 3:
        if direction == 0 :
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 2, arr)
        elif direction == 1 :
            arr = watch(x, y, 1, arr)
            arr = watch(x, y, 2, arr)
        elif direction == 2 :
            arr = watch(x, y, 1, arr)
            arr = watch(x, y, 3, arr)
        elif direction == 3 :
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 3, arr)

    elif type == 4:
        if direction == 0 :
            arr = watch(x, y, 1, arr)
            arr = watch(x, y, 2, arr)
            arr = watch(x, y, 3, arr)
        elif direction == 1 :
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 2, arr)
            arr = watch(x, y, 3, arr)
        elif direction == 2 :
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 1, arr)
            arr = watch(x, y, 3, arr)
        elif direction == 3 :
            arr = watch(x, y, 0, arr)
            arr = watch(x, y, 1, arr)
            arr = watch(x, y, 2, arr)
    elif type == 5:
        arr = watch(x, y, 0, arr)
        arr = watch(x, y, 1, arr)
        arr = watch(x, y, 2, arr)
        arr = watch(x, y, 3, arr)
    return arr

def count_blocks(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt +=1
    return cnt
# print()
ans = 999
import copy
for case in dir_case:
    office_data = copy.deepcopy(arr)
    for index,direction in enumerate(case):
        office_data = simulation(cctv[index][0],cctv[index][2],cctv[index][1],direction,office_data)
    # ans = min(ans,count_blocks(office_data))
    if count_blocks(office_data) <= ans:
        ans = count_blocks(office_data)
        # print(*office_data,sep='\n',end='\n\n')

print(ans)




