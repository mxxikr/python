"""
Again, the code is broken, you need to create 4 functions.
    - add_to_dict: Add a word to a dict.
    - get_from_dict: Get a word from inside a dict.
    - update_word: Update a word inside of the dict.
    - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(a_dict, a_word="", a_def=""):
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


def get_from_dict(a_dict, a_word="", a_def=""):
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

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


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


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

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