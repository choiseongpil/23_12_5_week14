def solution(numbers):
    if len(numbers) > 1000000:           # numbers의 길이를 1000000으로 제한 넘으면 오류 발생
        raise ValueError("Error: The length of 'numbers' exceeds the limit of 1000000")

    s]      # 각 원소의 길이를 1000으로 제한하고 문자열로 변환이 목적이지만 현재 코드를 돌려보면 왜인지 오류발
    numbers = [str(i)[:1000] for i in numbers]  
    for num in numbers:
        if len(num) > 1000:
            raise ValueError(f"Error: The length of an element ({num}) exceeds the limit of 1000")

    numbers.sort(key=lambda x: x*3, reverse=True)      #각 원소를 3번씩 곱해서 서로 비교해 더 큰 문자열로 만들 때 오류가 없기 위한것
    answer = str(int(''.join(numbers)))

    return answer

# 예시
try:
    numbers = [8, 30, 17, 2, 23, 11111]
    result = solution(numbers)
    print(result)
except ValueError as e:
    print(e)
