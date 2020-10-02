# Count how many times a character appears in a string
a_string = (str(input("Please enter a string: ")))
a_character = (str(input("Please enter character: ")))
len(a_string)
print("It appears in your string", a_string.count(a_character), "time(s)" )



# Number-converter

num1 = int(input("Please enter a number: "))
num_to_words = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

for num1 in str(num1):

    print(num_to_words[int(num1)], end=" ")























