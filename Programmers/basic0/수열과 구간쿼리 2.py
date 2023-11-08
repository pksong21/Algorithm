
def solution(arr, queries):
    answer = []
    for i in queries:
        arr2=[]
        for j in range(i[0], i[1]+1):
            if arr[j]>i[2]:
                arr2.append(arr[j])
        if len(arr2)==0:
            answer.append(-1)
            continue
        arr2.sort()
        answer.append(arr2[0])
    return answer