from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        self.stop_table = HashTable(191)
        try:
            in_file = open(filename)
        except:
            raise FileNotFoundError
        words=in_file.read()
        words=words.split('\n')
        for item in words:
            self.stop_table.insert(item, None)
        in_file.close()
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

    def load_concordance_table(self, filename):
        self.concordance_table = HashTable(191)
        try:
            in_file = open(filename)
        except:
            raise FileNotFoundError
        line_num=1
        for line in in_file:
            line=line.split()
            for word in line:
                if self.del_punctuation(word)==None:
                    continue
                if type(self.del_punctuation(word))==list:
                    idx=line.index(word)
                    word = self.del_punctuation(word)
                    for i in range(len(word)):
                        line.append(word[i])
                    continue
                word=self.del_punctuation(word)
                if self.concordance_table.in_table(word) and not self.stop_table.in_table(word):
                    line_list = (self.concordance_table.get_value(word))
                    if line_num not in line_list:
                        line_list.append(line_num)
                        self.concordance_table.hash_table[self.concordance_table.get_index(word)] = (word, line_list)
                elif not self.stop_table.in_table(word):
                    self.concordance_table.insert(word, line_num)
            line_num+=1
        in_file.close()

        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""

    def write_concordance(self, filename):
        out_file = open(filename, 'w')
        words = self.concordance_table.get_all_keys()
        words.sort()
        for i in range(len(words)):
            if words[i]=='':
                continue
            out_file.write(words[i] + ':')
            for val in self.concordance_table.get_value(words[i]):
                out_file.write(' ' + str(val))
            if i!= len(words)-1:
                out_file.write('\n')
        out_file.close()


        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""

    def del_punctuation(self, word):
        word = word.lower()
        for char in word:
            if char in string.punctuation:
                if char == "'":
                    word = word.replace(char, '')
                else:
                    word = word.replace(char, ' ')
        try:
            float(word)
            return None
        except:
            pass
        word = word.strip()
        if " " in word:
            return word.split()
        return word

