import random

# this function takes a string and returns a string with all the words reversed
# e.g. reverse("one two three") returns "three two one"
def reverseWords(s):
    # you may find these useful: 
    # 'a b c'.split() will return ['a','b','c']
    # ' '.join(['a','b','c']) will return 'a b c'
    # new_list = [] # create place holder list
    # split_list = s.split() # break single string into a list of word strings.
    # for word_idx in range(len(split_list)-1,-1,-1): # starting from the last position, going to the first position, in (reverse) step size 1
    #     new_list.append(split_list[word_idx]) # append (to the end) of new_list the word from split_list at position word_idx.

    # return ' '.join(new_list) # convert list of word strings to single string with space

    return ' '.join([word for word in s.split()[::-1]])

def getWordCount2(my_string):
    # iterate through each word in the string
    my_dict={}
    list_of_words = my_string.split()
    for word in list_of_words:
        if word not in my_dict:
            my_dict[word]=1
        else:
            my_dict[word] += 1

    return my_dict

def getWordFrequencies2(my_string):
    # iterate through each word in the string
    my_dict={}
    list_of_words = my_string.split() # this creates a list of strings, each string is one word
    count = len(list_of_words) # we want to know the total number of words in the string
    for word in list_of_words:
        if word not in my_dict:
            my_dict[word]=1/count
        else:
            my_dict[word]+=1/count # this is the same as my_dict[word]=my_dict[word]+1/count

    return my_dict

def generateSentence2(word_freq_dict):
    vocabulary_list = list(word_freq_dict.keys())
    vocabulary_weights = list(word_freq_dict.values())
    random_string=''
    while True:
        random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
        random_string += random_word[0] + ' '
        if random_word[0] == '.':
            break

    # random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
    # while not random_word[0] == '.':
    #     random_string += random_word[0] + ' '
    #     random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
    # random_string += '.'


    return random_string

#HOMEWORK FUNCTIONS---------------------------------------------------------------------------------------------------


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
    word_picked = list(first_dict.keys())
    frequencies = list(first_dict.values())
    word = random.choices(word_picked, weights=frequencies, k = 1)  
    first_word = word[0]
    return first_word  

def create_nested_pair_dict(word_list, pair_list):
    nested_dict = {}
#NEED TO FIGURE OUT WHY ITS NOT PRINTING THE RIGHT PERCENTAGES<--
    for word in word_list:
        # Initialize an inner dictionary for the current word
        nested_dict[word] = {}

        # Collect unique pairs that start with the current word
        unique_pairs = set(pair for pair in pair_list if pair.split()[0] == word)

        # Count the total occurrences of the current word as the first word in pairs
        word_count = len(unique_pairs)

        for pair in unique_pairs:
            # Calculate the frequency and add it to the inner dictionary
            frequency = 1/word_count
            nested_dict[word][pair] = frequency

    return nested_dict

def generateSentence(nested_dict, first_word):
    sentencelst = []
    sentencelst.append(first_word)
    current_word = first_word
    while '.' != current_word:
        target = nested_dict[current_word]
        #print(target)
        #break
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
    print(final_creation)

if __name__=='__main__':
    # print(reverseWords('one two three'))
    # print(getWordCount2('cat dog dog penguin .'))
    # print(getWordFrequencies2('cat dog dog penguin .'))
    # vocabulary_dict = getWordFrequencies2('cat dog dog penguin .')
    # print(generateSentence(vocabulary_dict))
    my_string = "hello my name is my name the ball went . to the car and my name is steven hi ."
    pair_lst = getWordPairs(my_string)
    word_lst = my_string.split()

    nested_pair_dict = create_nested_pair_dict(word_lst, pair_lst)

    x_word = firstWord(my_string)
    print(generateSentence(nested_pair_dict, x_word))




