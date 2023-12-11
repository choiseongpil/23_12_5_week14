def solution(my_string, target):
  answer = 0

  #제한조건을 만족하기 위해서 넣음 앞부분은 이하제한, 뒷부분은 소문자 판별
  if 1 <= len(my_string) <=100 and 1<= len(target) <=100 and my_string.islower() and target.islower():   
    if target in my_string:          #if in 함수를 사용해서 B안에 A의 문자열이 있는지 따짐
      answer = 1                  #만약 존재하면 1 아니면 0 반환
      
  return answer

#예시로 string에 qwerty, target에 qwe를 대입 결과는 1임을 돌려보면 알 수 있음
my_string = "qwerty"
target = "qwe"
answer = solution(my_tsring, target)
print(answer)
