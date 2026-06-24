# try catch exception

# try:
#     age = int(input("What's your age? "))
# except ValueError:
#     print("The input is not an integer.")
#     age = int(input("What's your age? "))

# if age >= 18:
#     print("You can drink.")
    
    
# Use print
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

print("Pages: ", pages)
print("Word per page: ", word_per_page)
total_words = pages * word_per_page
print(total_words)