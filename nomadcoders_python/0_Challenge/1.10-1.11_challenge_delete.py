def get_from_dict(a_dict="", a_word="", a_def=""):
    if type(a_dict) is str:
        print(("You need to send a dictionary. You sent: <class 'str'>"))
    else:
        if a_word == "":
            print("You need to send a word to search for.")
        elif a_word not in my_english_dict:
            print(f"{a_word} was not found in this dict.")
        else:
            print(a_word + ": "+ a_dict[a_word])

def delete_from_dict(a_dict, a_word="", a_def=""):
    if type(a_dict) is str:
        print(("You need to send a dictionary. You sent: <class 'str'>"))    
    elif a_word == "":
        print("You need to specify a word to delete.")
    elif a_word not in a_dict:
        print(f"{a_word} is not in this dict. Won't delete.")
    else: 
        del a_dict[f"{a_word}"]
        print(f"{a_word} has been deleted.")


my_english_dict = {'kimchi' : 'Food from the gods.'}

print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\