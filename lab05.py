""""
The program is trying to translate a sentence captured an user input.
We first read text file.
then from the text fule, we create a list of strings from each lines in the text file.
Then we create dictionary from list.
Once the text file has been read into memory, we close the file.

we then define a function for translating which envolves splitting the user input (sentence) into 
an array of strings ["enjoy", "the", "excellent", "band", "tonight"]

once we have the array of strings representing the user's input setence, we
loop through each words, find the key matching the word and rreturn back the value tied to the word
in our dictionary

after each word is trnaslated, we then
print out the translated sentence to the user.
"""