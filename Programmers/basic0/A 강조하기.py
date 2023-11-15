# 문자열 myString이 주어집니다.
# myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
#
def solution(myString):
    answer = ''
    #my String 에서 문자하나씩 i로 가져옴
    for i in myString :
        #i가 "A"나 "a" 라면 answer 에 "A"로 추가
        if i == "a"or i=="A":
            answer += "A"
        #아니면 i를 lower()이용 소문자로 만들어서 answer 에 추가
        else :
            answer += i.lower()
    return answer