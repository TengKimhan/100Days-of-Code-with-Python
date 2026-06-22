def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    print(str(true_count) + str(love_count))
        