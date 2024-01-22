import random

def getWordPairs(my_string):
    words = my_string.split()
    pair_lst = []

    # Getting the pairs and joining strings
    for i in range(len(words) - 1):
        #length has to be -1 since i+1 at the end would be out of range
        word_pair = ' '.join([words[i], words[i + 1]])
        pair_lst.append(word_pair)

    return pair_lst

def firstWord(my_string):
    firstlst = my_string.split()
    first_dict = {}
    count = len(firstlst)

    for word in firstlst:
        if word not in first_dict:
            first_dict[word] = 1/count
        else:
            first_dict[word] += 1/count
    vocab_dict = list(first_dict.keys())
    vocab_freq = list(first_dict.values())
    word = random.choices(vocab_dict, weights=vocab_freq, k = 1)  
    first_word = word[0]
    return first_word  

def nestPairDict(wl, pl):
    nested_dict = {}
#NEED TO FIGURE OUT WHY ITS NOT PRINTING THE RIGHT PERCENTAGES<--
    for word in wl:
        nested_dict[word] = {}
        uniquePairs = []
        for pair in pl:
            beginPair = pair.split()[0]
            if beginPair != word:
                continue
            if pair not in uniquePairs:
                uniquePairs.append(pair)
# Count the total occurrences of the current word as the first word in pairs
        word_count = len(uniquePairs)
        for pair in uniquePairs:
# Calculate the frequency and add it inside the dictionary (inner dict)
            frequency = 1/word_count
            nested_dict[word][pair] = frequency

    return nested_dict

def generateSentence(nested_dict, first_word):
    sentencelst = []
    sentencelst.append(first_word)
    current_word = first_word
    while '.' != current_word:
        target = nested_dict[current_word]
        vocabulary_list = list(target.keys())
        vocabulary_weights = list(target.values())
        random_word = random.choices(vocabulary_list, weights=vocabulary_weights, k = 1)
        word_fix = random_word[0]
        temp_split = word_fix.split()
        next_word = temp_split[1]
        sentencelst.append(next_word)
        current_word = next_word
    final_creation = ''
    for i in range(len(sentencelst)):
        final_creation += sentencelst[i] + ' '
    return final_creation


if __name__=='__main__':
    my_string = "hello my name is my name the ball went . to the car and my name is steven hi ."
    pair_lst = getWordPairs(my_string)
    word_lst = my_string.split()
    nested_pair_dict = nestPairDict(word_lst, pair_lst)
    x_word = firstWord(my_string)
    print(generateSentence(nested_pair_dict, x_word))