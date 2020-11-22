"""
Conditionals in Python
"""
programming_language = input("Please write your favorite programming language:")
programming_languages = [
    "PHP",
    "Python",
    "Ruby",
    "Java",
    "C",
    "C++",
    "R",
    "JavaScript",
    "TypeScript",
    "Elixir",
    "Go"
]

print(f"The available programming languages are: \n {programming_languages}")

if programming_languages.__contains__(programming_language):
    if not programming_language == programming_languages[0]:
        print(f"For me too, {programming_language} is one of my favorites")
    else:
        print(f"Enjoy {programming_language} by coding some software applications!")
else:
    programming_languages.append(programming_language)

print(f"The available programming languages are: \n {programming_languages}")