def solution(planet_age):
    if not planet_age.islower():          #소문자인지 판별한다.
        raise ValueError("lowercase alphabet")             #소문자가 아니면 오류가 뜬다

    answer = 0

    for char in planet_age:                            #각 알파벳을 숫자로 변환하는 과정
        answer = answer * 10 + (ord(char) - ord('a'))

    if answer > 1000:                              #만약 1000이하가 아니면 오류가 뜸
        raise ValueError("not answer <= 1000")

    age = int(planet_age)                          #만약 자연수가 아니라면 오류가 뜸
    if age <= 0:
        raise ValueError("나이는 자연수여야 합니다.")

    return answer

#코드를 테스트하기 위해서 예제를 들었다.
try:                    #try except라는 것으로 오류가 떳을 시 그 오류를 출력함
    planet_age = "xyz"  #xyz라는 알파벳을 넣었고 계산 결과 1000이 넘어가니 2번째 오류가 뜰 것이다.
    number_age = solution(planet_age)
    print(number_age)
except ValueError as e:
    print(f"Error: {e}")
