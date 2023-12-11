def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    answer = ''
    
    # 제한사항에 따라 길이 확인
    if 1 <= len(letter) <= 1000: # 공백을 기준으로 Morse 부호를 분리하고 해독하여 영어 소문자로 변환
        words = letter.split(' ')
        for word in words:
            answer += morse.get(word, ' ')  # 해당 Morse 부호가 없으면 공백을 추가
    
    return answer

# 예제 테스트
letter = ".... . .-.. ---  .-- --- .-. .-.. -.."
answer = solution(letter)
print(result)  # 예상 결과: hello world
