def add_to_dict(a_dict, a_word, a_def=""):
    if type(a_dict) is str:
        print("You need to send a dictionary. You sent: <class 'str'>")
    else:
        if a_def == "":
            print("You need to send a word and a definition.")
        elif a_word in my_english_dict:
            print(f"{a_word} is already on the dictionary. Won't add.")
        else:
            a_dict[a_word] = f"{a_def}" 
            print(f"{a_word} has been added.")

my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")
