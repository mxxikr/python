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

def update_word(a_dict, a_word="", a_def=""):
    if type(a_dict) is str:
        print(("You need to send a dictionary. You sent: <class 'str'>"))
    else:
        if a_def =="":
            print("You need to send a word and a definition to update.")
        elif a_word not in a_dict:
            print(f"{a_word} is not on the dict. Can't update non-existing word")
        else: 
            a_dict[a_word] = f"{a_def}"  
            print(f"{a_word} has been updated to: {a_def}")

my_english_dict = {'kimchi' : 'The source of life.'}

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")