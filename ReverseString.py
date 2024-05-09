sentence = "My name is Shubham"

words = sentence.lower()
words = words.split()

reverse = " ".join(word[::-1] for word in words)
print(reverse)


