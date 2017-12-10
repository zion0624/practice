login=input("아이디를 입력하세요.\n")
members=['zion','jspark','minje','hyun jun']
for member in members:
    if member==login:
        print("hello "+member)
        import sys    #for 문을 종료하는 명령어
        sys.exit()
print('who are you')