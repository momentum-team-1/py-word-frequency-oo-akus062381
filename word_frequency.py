STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
import string

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        opened_file = open(self.filename)
        read_contents = opened_file.read()
        opened_file.close()
        return read_contents


class WordList:
    def __init__(self, text):
        self.text = text
        self.words = []

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        just_words = self.text.strip()
        lowercase_words = just_words.lower()
        self.word_strings = lowercase_words.split()
        # print(self.word_strings)
        self.sorted_words = sorted(self.word_strings)
        # print(self.sorted_words)

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        self.stripped_words= [word for word in self.sorted_words if not word in STOP_WORDS]
        # print(self.stripped_words)   

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        self.freqs = {}
        for word in self.stripped_words:
            self.freqs[word] = self.freqs.get(word, 0) + 1
            return self.freqs
        

class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        most_used = []
        most_used_words = []
        x = 0
        for item in self.freqs.items():
            if x < 10:
                most_used.append(item)
                most_used_words.append(item[0])
                x += 1
        most_frequent = max(most_used_words, key=len)
        for item in most_used:
            print(len.rjust(15) , ' | ', str(value).rjust(2), value * ("*"))


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
