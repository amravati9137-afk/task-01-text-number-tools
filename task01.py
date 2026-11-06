#Task 01 - Text and number tools

#function 1: Count words
def count_words(sentence):
    words=sentence.split()
    return len(words)

#function 2: find longest word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return "No words found"

    return max(words,key=len)

#function 3: Reverse sentence
def reverse_sentence(sentence):
    return sentence[::-1]

#function 4: Check prime number
def is_prime(number):
    if number<= 1:
        return false

    for i in range(2, int(number **0.5) +1):
        if number % i ==0:
            return false

    return True

#main program
print("===== TEXT AND NUMBER TOOLS =====")

sentence= input("enter a sentence:")

print("\n----text results----")
print("Word count:",count_words(sentence))
print("Longest word:",longest_word(sentence))
print("reversed sentence:",reverse_sentence(sentence))

number = int(input("\nenter a number: "))
print("\n----number results----")

if is_prime(number):
    print(number,"is a prime number")
else: 
    print(number,"is not a prime number")
