f = open("C:/Users/mxxikr/Documents/readline.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

f = open("C:/Users/mxxikr/Documents/readline.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

while 1:
    data = input()
    if not data: break
    print(data)
