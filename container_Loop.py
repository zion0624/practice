members=['zion','park','minje']
i=0
while i<len(members): #리스트(컨테이너)의 원소의 개수만큼 반복
    print(members[i])
    i=i+1

print("_____________")

members=['zion','park','minje']
for member in members: # in뒤에 리스트(컨테이너)의 이름을 쓰고 in앞에 리스트의 원소에 해당하는 이름을 지어줌
    print(member)      # for in 문은 문법적 설탕ㅋ

print("_____________")
for item in range(5,11): #for in 문을 활용하여 반복문 처럼 사용하기
    print(item)       #range() 함수는 0부터 ()안에 숫자까지 반복
                      #range(a,b)일 경우 a~b까지 반복