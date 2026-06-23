# Dictionary

programming_languages = {
    "Python": "A high-level, interpreted programming language known for its readability and versatility.",
    "JavaScript": "A versatile programming language primarily used for web development to create interactive effects within web browsers.",
    "Java": "A widely-used, class-based, object-oriented programming language designed to have as few implementation dependencies as possible.",
    "C++": "An extension of the C programming language that includes object-oriented features, widely used for system/software development and game programming.",
    "Ruby": "A dynamic, open-source programming language with a focus on simplicity and productivity, known for its elegant syntax.",
    "Go": "A statically typed, compiled programming language designed for simplicity and efficiency, developed by Google.",
    "Swift": "A powerful and intuitive programming language developed by Apple for iOS, macOS, watchOS, and tvOS app development."
}

print(f"Python: {programming_languages['Python']}")
print(f"Python: {programming_languages.get('Python')}")

# dict.items() method returns an object of key value pairs
for language, description in programming_languages.items():
    print(f"{language}: {description}")
    
# access the keys of the dictionary
for key in programming_languages:
    print(key)
    
# access the keys of the dictionary using the keys() method
for key in programming_languages.keys():
    print(key)
    
# access the values of the dictionary
for value in programming_languages.values():
    print(value)

    
programming_languages["C#"] = "A modern, object-oriented programming language developed by Microsoft as part of the .NET framework."
print(f"C#: {programming_languages['C#']}")