import calculator
import strings
import file_io
import generate_sentence
import sys

print(sys.argv)

# check if user wants calculator functionality
if '-c' in sys.argv:
    # the function name starts after '-c'
    function_name_idx = sys.argv.index('-c')+1
    # guess that the 2 integeter inputs start after function name
    a_idx = sys.argv.index('-c')+2
    b_idx = sys.argv.index('-c')+3
    # try to see if the indices for a and b are actually integers or not, and loop to find them.
    while True:
        try:
            a = int(sys.argv[a_idx])
            b = int(sys.argv[b_idx])
            break
        except:
            a_idx +=1
            b_idx +=1

    # get all function names as a list of strings
    # if there are many function names, e.g. main.py -c sum product 4 5
    # and we want to calculate both the sum and the product
    function_str_list = sys.argv[2:len(sys.argv)-2] # NOTE: This line is problematic!
    results=[] # for each function in the list, compute the result and save in list
    for function_str in function_str_list:
        try:
            function = getattr(calculator,function_str)
            if not '-o' in sys.argv or '-i' in sys.argv:
                print(function(a,b))
            else:
                results.append(str(function(a,b)))
        except:
            if not '-o' in sys.argv:
                print(f'{function_str} isn\'t defined for calculator')
            else:
                results.append(f'{function_str} isn\'t defined for calculator')
# check if user wants string functionality
# python main.py -s reverseWords please reverse me
if '-s' in sys.argv:
    if 'reverseWords' in sys.argv:
        my_string = ' '.join(sys.argv[3:])
        print(strings.reverseWords(my_string))
        
        if '-i' in sys.argv:
            file_name_idx = sys.argv.index('-i')+1
            file_content = file_io.getFileContent(sys.argv[file_name_idx])
            print(strings.reverseWords(file_content))

# if there's an input file, read and print.
if '-o' in sys.argv:
    file_name_idx = sys.argv.index('-i')+1
    #Gets what the file says
    file_content = file_io.getFileContent(sys.argv[file_name_idx])
    my_string = file_content.strip('"')
    #print(new_content)
    pair_lst = generate_sentence.getWordPairs(my_string)
    word_lst = my_string.split()
    first_word = generate_sentence.firstWord(my_string)
    nested_dict = generate_sentence.nestPairDict(word_lst, pair_lst)
    creation_sentence = generate_sentence.generateSentence(nested_dict, first_word)
    print(creation_sentence)
    file_name_idx = sys.argv.index('-o')+1
    file_io.writeToFile(sys.argv[file_name_idx], creation_sentence)

elif '-i' in sys.argv and len(sys.argv)==3:
    file_name_idx = sys.argv.index('-i')+1
    #Gets what the file says
    file_content = file_io.getFileContent(sys.argv[file_name_idx])
    my_string = file_content.strip('"')
    #print(new_content)
    pair_lst = generate_sentence.getWordPairs(my_string)
    word_lst = my_string.split()
    first_word = generate_sentence.firstWord(my_string)
    nested_dict = generate_sentence.nestPairDict(word_lst, pair_lst)
    creation_sentence = generate_sentence.generateSentence(nested_dict, first_word)
    print(creation_sentence)
else:
    print("Failed execution, please try again")

# write the contetent of list "results" to output file

