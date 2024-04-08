f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

with open("test.txt", 'w') as f1:
    f1.write("Life is too short!")
with open("test.txt", 'r') as f2:
    print(f2.read())
