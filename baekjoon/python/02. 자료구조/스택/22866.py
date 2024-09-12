n = int(input())
buildings = list(map(int, input().split()))
stackRight = []
stackLeft = []
buildingCount = [0]*n
nearBuilding = [1000000]*n
#빌딩은 오른쪽으로 이동, 시선은 왼쪽 바라보기
for idx, height in enumerate(buildings):
    while stackRight and buildings[stackRight[-1]] <= height:
        stackRight.pop()

    buildingCount[idx] += len(stackRight)

    #가까운 빌딩 갱신
    if stackRight :
        if abs(idx-stackRight[-1]) < abs(nearBuilding[idx] - idx) :
            nearBuilding[idx] = stackRight[-1]

    stackRight.append(idx)

#빌딩은 오른쪽으로 이동, 시선은 왼쪽 바라보기
for idx in range(n - 1, -1, -1):
    height = buildings[idx]

    while stackLeft and buildings[stackLeft[-1]] <= height:
        stackLeft.pop()
    buildingCount[idx] += len(stackLeft)

    #가까운 빌딩 갱신
    if stackLeft :
        if abs(idx-stackLeft[-1]) < abs(nearBuilding[idx] - idx) :
            nearBuilding[idx] = stackLeft[-1]

    stackLeft.append(idx)

for i in range(n) :
    if buildingCount[i] == 0 :
        print(0)
    else :
        print(buildingCount[i], nearBuilding[i]+1)
