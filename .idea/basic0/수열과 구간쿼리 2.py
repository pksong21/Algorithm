
def solution(arr, queries):
    answer = []

    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]
        t=[]

        if e + 1 == len(arr):
            for j in range(len(arr)):
                if arr[j] > k:
                    t.append(arr[j])
        else:
            for j in range(s,e+1):
                if arr[j] > k:
                    t.append(arr[j])
        t.sort()
        if len(t) == 0:
            answer.append(-1)
        else:
            answer.append(t[0])


    return answer