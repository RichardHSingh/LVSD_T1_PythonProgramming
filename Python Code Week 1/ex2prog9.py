#============== CALCULATING VOWELS IN GIVEN WORD =====================

# value of vowels given and checkign given work has these letters in it
def count_vowels(word): 
    # vowel values
    vowels = "aeiou"
    count = 0 
    for char in word: 
        # .lower will change all input to lower case letters so output can be accurate even if CAPS used
        if char.lower() in vowels: 
            count += 1 
    return count
    #need to return count not the function

count_vowels("HYPOTHEMIA")
# using the value, check against word to see how many of those vowels are in particular word

