f = open("test.txt", 'r')
txt = f.read()
f.close()

txt = txt.replace("java", "python")

f = open("test.txt", 'w')
f.write(txt)
f.close()