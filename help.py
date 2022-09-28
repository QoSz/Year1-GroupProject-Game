# ######################################################################################################## #

# Module to help program a little easier
import string

###################################################################################
#List of words to be skipped.
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']
###################################################################################



# #################################################################################
# A function to easily make a new line.

def ClearLine():
	print(" ")

# #################################################################################



###################################################################################
#A function to remove any useless words.

def filter_words(words, skip_words):
        goodwords = []
        for word in words:
                if word not in skip_words:
                        goodwords.append(word)
        return goodwords

###################################################################################


###################################################################################
#A function to remove any punctuation.
def remove_punct(text):
        no_punct = ""
        for char in text:
                if not (char in string.punctuation):
                        no_punct = no_punct + char

        return no_punct

###################################################################################



###################################################################################
#A function to normalise the users input.
def normalise_input(user_input):
        no_punct = remove_punct(user_input).lower()
        filteredwords = filter_words((no_punct).split(), skip_words)
        return (filteredwords)
