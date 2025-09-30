# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
def counting_vowels_and_consonants(paragraph):
    vowels_list = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for letter in paragraph:
        if letter in vowels_list:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
    return (vowel_count, consonant_count)

print(counting_vowels_and_consonants("You’re curious about the average number of vowels compared to consonants in a paragraph."))



# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)
def average_vowels_and_consonants(paragraph):
    sentence_vowels = []
    sentence_consonants = []
    sentences = paragraph.split(".")
    first_two_sentences = sentences[0].split("!")
    sentences.pop(0)
    sentences.insert(0, first_two_sentences[0])
    sentences.insert(1, first_two_sentences[1])
    sentences.pop(len(sentences) - 1)
    for i in range(len(sentences)):
        sentence_vowels.append(counting_vowels_and_consonants(sentences[i])[0])
        sentence_consonants.append(counting_vowels_and_consonants(sentences[i])[1])
    total_vowels = 0
    total_consonants = 0
    for i in range(len(sentences)):
        total_vowels += sentence_vowels[1]
        total_consonants += sentence_consonants[i]
    average_vowels = total_vowels // len(sentences)
    average_consonants = total_consonants // len(sentences)
    return len(sentences), average_vowels, average_consonants
    
print(f"This paragraph has {average_vowels_and_consonants(paragraph)[0]} sentences.  On average, each sentence contains {average_vowels_and_consonants(paragraph)[1]} vowels and {average_vowels_and_consonants(paragraph)[2]} consonants")
# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
