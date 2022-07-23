#알파벳 소문자로 단어 입력
#첫째줄에 팰린드롬이면 1 아니면 0을 출력
word = input()

for i in range(len(word)//2):
    if(word[i] != word[-i-1]):
        pal = 0
    else:
        pal = 1   
print(pal)  