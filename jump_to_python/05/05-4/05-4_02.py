f = open('foo.txt', 'w')
try :
    4 / 0
finally:
    f.close()