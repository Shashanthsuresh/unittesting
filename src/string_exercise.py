class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        reverse=input_str[::-1]
        return reverse
    

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        if character in vowel:
            return True
        else:
            return False
        

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest=sentence.split()
        return max(longest,key=len)
    

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        longest_string=text.split()
        return list(map(len,longest_string))



    
