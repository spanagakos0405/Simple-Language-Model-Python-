# given a file object, f.read() will return the contents of f as a single string

# given a filename (as a string), this will return the text of a file as a single string
def getFileContent(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()

    return content

# given a file object and a string s, f.write(s) will write a single string to file
def writeToFile(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()

# note: there is also readlines() and writelines([list_of_strings])
# that work with lists of strings.