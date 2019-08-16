import unittest
import filecmp
import subprocess
from concordance import *

use_diff = False

class TestList(unittest.TestCase):
    #Tests file that does not exist
    def test_load_stop_table1(self):
        with self.assertRaises(FileNotFoundError):
            conc = Concordance()
            conc.load_stop_table("sike.txt")
    #Checks that stop words loads all the stop words into the hash table
    def test_load_stop_table2(self):
        conc = Concordance()
        conc.load_stop_table('stop_words.txt')
        self.assertEqual(conc.stop_table.get_all_keys(),['only', 'off', 'your', 'had', 'would', 'yet', 'me', 'there', 'has', 'should', 'were', 'am', 'an', 'my', 'might',
     'its', 'as', 'at', 'these', 'however', 'rather', 'no', 'be', 'from', 'just', 'for', 'cannot', 'said', 'wants',
     'she', 'how', 'by', 'of', 'a', 'across', 'them', 'then', 'i', 'our', 'on', 'nor', 'not', 'or', 'who', 'they',
     'what', 'does', 'why', 'with', 'too', 'neither', 'do', 'their', 'about', 'all', 'hers', 'among', 'her', 'whom',
     'own', 'could', 'let', 'while', 'most', 'can', 'and', 'must', 'says', 'least', 'also', 'other', 'so', 'twas',
     'any', 'this', 'when', 'been', 'because', 'have', 'ever', 'but', 'else', 'did', 'may', 'some', 'he', 'to', 'will',
     'often', 'say', 'got', 'him', 'was', 'the', 'his', 'which', 'if', 'us', 'after', 'either', 'in', 'is', 'it', 'tis',
     'every', 'are', 'able', 'almost', 'we', 'you', 'dear', 'get', 'into', 'where', 'than', 'since', 'that', 'like',
     'likely'])

    #Tests a file that does not exist
    def test_load_concordance_table1(self):
        with self.assertRaises(FileNotFoundError):
            conc = Concordance()
            conc.load_stop_table("sike.txt")

    #Tests a concordance table with a file that has no punctuation
    def test_load_concordance_table2(self):
        conc = Concordance()
        conc.load_stop_table('stop_words.txt')
        conc.load_concordance_table('file1.txt')
        self.assertEqual(conc.concordance_table.get_all_keys(), ['washington', 'stop', 'fourscore', 'years', 'ago', 'quicksort', 'topology', 'correctly', 'seven', 'handled', 'earthquake', 'words'])
    #Tests a concordance table with a file that contains punctuation
    def test_load_concordance_table3(self):
        conc = Concordance()
        conc.load_stop_table('stop_words.txt')
        conc.load_concordance_table('file2.txt')
        self.assertEqual(conc.concordance_table.get_all_keys(), ['punctuation', 'american', 'quicksorts', 'time', 'consuming', 'earthquake', 'african', 'line'])

    #Tests given file 1
    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
    #Tests given file 2
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))
    #Tests the given declaration file
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    #Tests an empty file
    def test_04(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty.txt")
        conc.write_concordance("empty_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb empty_con.txt empty_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

    #Tests a file of all stop words
    def test_05(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("all_stop.txt")
        conc.write_concordance("all_stop_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb all_stop_con.txt empty_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("all_stop_con.txt", "empty_sol.txt"))

    #Tests a file that contains one word repeated on a line
    def test_06(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("dog.txt")
        conc.write_concordance("dog_con.txt")
        if use_diff:
            err = subprocess.call("diff -wb dog_con.txt dog_sol.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("dog_con.txt", "dog_sol.txt"))



if __name__ == '__main__':
   unittest.main()
