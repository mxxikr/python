languages = ['python', 'perl', 'c', 'java']

for lang in languages: # 줄맞춤(들여쓰기) 중요
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")