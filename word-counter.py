print("What's on you mind today?")

response = input("Enter your response: ")

words_split = response.split()

word_count = len(words_split)


print("Wow, you just answered me in {}".format((word_count)),"words!")
