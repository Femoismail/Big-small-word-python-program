textfile = open("big-small word program/textfile.txt", "w")  # creates a textfile

textfile.write(input("Please enter your sentence :")) # user inputs a text which is written to the textfile

textfile.close() 




open_textfile = open("big-small word program/textfile.txt", "r") # opens the file in read only

sentence = open_textfile.read() 




list_symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.','/','\'','}',')','&','!','_','#','"',";",">","?","="]  # list of special characters

for symbol in list_symbols:    # loops through the list of symbols to find any symbol which is in the sentence and removes the symbol from the sentence
    split_sentence = sentence.split(symbol) 
    new_sentence = " ".join(["".join(y) for y in split_sentence])
    sentence = new_sentence




    
new_split_sentence = sentence.split() # splits the sentence by each space in the sentence and assigns each word to a list.

big_word_length = 0  # length check for big word

big_word_list = [] # adds all words where the length of the word is bigger then big_word_count





for word in new_split_sentence:   # loops through each word in the list to find the length of the word and compares the length of the word to big_word_length and if the length of the word is greater than big_word_length it assigns the length of the word to big_word_length and it assigns the word to big_word_list
    if len(word) > big_word_length:
        big_word_length = len(word)
        big_word_list.append(word)

small_word_length = big_word_length # assigned the length of big_word_length to samll_word_length as a starting point to find the smallest word

small_word_list = []

for word in new_split_sentence:  # loops through each word in the list to find the length of the word and compares the length of the word to small_word_length and if the length of the word is less than small_word_length it assigns the length of the word to small_word_length and it assigns the word to small_word_list
    if len(word) < small_word_length:
        small_word_length = len(word)
        small_word_list.append(word)

print("BIGGEST WORD")
print()
print(f'Longest word in sentence = {big_word_list[-1]}')
print()
print(f'Length of longest word in sentence = {big_word_length}')
print()
print('SMALLEST WORD')
print()
print(f'Smallest word in sentence = {small_word_list[-1]}')
print()
print(f'Length of smallest word in sentence = {small_word_length}')



