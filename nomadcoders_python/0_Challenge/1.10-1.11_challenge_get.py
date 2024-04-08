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

my_english_dict = {}

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