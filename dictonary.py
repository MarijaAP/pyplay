import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    """
    English thesaurus dictionary that finds, and suggests word similarities until match is found.
    """
    word = word.lower()
    if word in data:
        for w in data[word]:
            print(w)
    else:
        #gets possible casesensitive matches in a possible_match list:
        possibile_match = get_close_matches(word, data.keys())
        #adds possible case-insensitive matches to the same list:
        for i in get_close_matches(word.upper(), data.keys()):
            possibile_match.append(i)
        for word in possibile_match:
            question = input(f"Did you mean {word}? Enter Y if yes or N if no? ")
            if question.lower() == "y":
                if word in data:
                    for w in data[word]:
                        print(w)
                    break
                else:
                    return "The word does not exist. Please double check it."
            else:
                #asks the user for each word in the possible_match list if it's a match:
                if possibile_match.index(word) == (len(possibile_match)-1):
                    print("Sorry, we did not find the word you are looking for")
                else:
                    continue

word = input("Enter a word: ")

translate(word)
