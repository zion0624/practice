def a3():            #함수 만들기
    print("aaa")     #def로 함수 정의하기
a3()

print("___________")

def b3():
    return 'bbb'     #return값이 def로 만든 함수값을 결정, return을 끝으로 함수의 정의가 끝난다
print(b3())          #return 뒤에 = 안씀 주의

print("___________")

def c(num):
    return 'c'*num
print(c(9))


print("___________")

def string(str,num):#여러개의 입력값
    return str*num
print(string("zion",4))


print("private님 return이 사알짝 이해가 안돼요")