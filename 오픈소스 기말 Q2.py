def solution(letter):
  morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
  
  answer = ''
  
  if 1 <= len(letter) <= 1000:              #제한조건을 만족하기위함
    words = letter.split(' ')               #공백으로 나누어져 있으니 스플릿을 이용해 나누고 해독하여 영어로 변환
    for word in words:
      if word:                               #연속된 공백이 아니면 처리
        if word in morse:                    #해당 모스부호가 존재하지 않으면 공백처리
          answer += morse[word]
        else:
          answer += ' '
  return answer

#예시로 든 것
letter = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."       #이것을 돌려보면 hello world를 얻을 수 있음
answer = solution(letter)
print(answer)
