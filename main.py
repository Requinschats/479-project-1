from pathlib import Path
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import os


def select_lowercase_string_array(string_array):
    return list(map(lambda string: string.lower(), string_array))


def select_stemmed_string_array(string_array):
    stemmer = PorterStemmer()
    return list(map(lambda string: stemmer.stem(string), string_array))


def select_tokenized_array(string):
    return word_tokenize(string)


def select_string_array_without_stop_words(string_array):
    english_stopwords = stopwords.words("english")
    return list(filter(lambda string: string not in english_stopwords, string_array))


def write_to_file(file_name, step, content):
    file = open("output" + "/" + step + "/" + file_name, 'w+')
    if isinstance(content, list):
        content = " ".join(content)
    file.write(content)


def main():
    for fileName in os.listdir("reuters21578")[:5]:
        print("Processing document: " + fileName)

        file_content = Path('reuters21578/' + fileName).read_text()
        write_to_file(fileName, "step-1", file_content)

        tokenized_file_content = select_tokenized_array(file_content)
        write_to_file(fileName, "step-2", tokenized_file_content)

        tokenized_file_content = select_lowercase_string_array(tokenized_file_content)
        write_to_file(fileName, "step-3", tokenized_file_content)

        tokenized_file_content = select_stemmed_string_array(tokenized_file_content)
        write_to_file(fileName, "step-4", tokenized_file_content)

        tokenized_file_content = select_string_array_without_stop_words(tokenized_file_content)
        write_to_file(fileName, "step-5", tokenized_file_content)


if __name__ == '__main__':
    main()
