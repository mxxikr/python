 
f = open("test.txt", 'a')
f.write(input("저장할 내용을 입력해주세요 : "))
f.write("\n")
f.close()


user_input = input("저장할 내용을 입력하세요 : ")

f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()
