def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(fname,"r") as f:
        for line in f:
            num_lines += 1
            word ="Y"
            for letter in line:
                if(letter !='' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if(i !=""and i !="\n"):
                        num_charc += 1

    print("number of word in text file:",num_words)
    print("number of line in text file:",num_lines)
    print("number of characters in text file :",num_charc)
    print("number of spaces in textfile:",num_spaces)
if __name__ == '__main__':
    fname = "file.txt"
    try:
        counter(fname)
    except:
        print('file not found')

