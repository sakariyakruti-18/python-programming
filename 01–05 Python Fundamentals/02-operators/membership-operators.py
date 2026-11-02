# Membership Operators

fruits = ["apple", "banana", "mango", "orange"]

print("Available fruits:", fruits)

fruit = input("Enter a fruit name to search: ").lower()

print("Fruit is available:", fruit in fruits)
print("Fruit is not available:", fruit not in fruits)

#with a string
text = input("Enter a sentence: ")
word = input("Enter a word to search: ")

print("Word exists in sentence:", word.lower() in text.lower())
print("Word does not exist in sentence:", word.lower() not in text.lower())

'''
Available fruits: ['apple', 'banana', 'mango', 'orange']
Enter a fruit name to search: graps
Fruit is available: False
Fruit is not available: True
Enter a sentence: 'where is tasty tasty graps?'
Enter a word to search: where
Word exists in sentence: True
Word does not exist in sentence: False
'''
