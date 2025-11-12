from stats import get_num_words, text_chars, sorted_chars
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
        return book

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) <= 1:
        explaination = "Usage: python3 main.py <path_to_book>"
        print(explaination)
        sys.exit(1)
        
    else:
        book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    chars_text = text_chars(text)
    print("--------- Character Count -------")
    sorted_characters = sorted_chars(chars_text)
    for char in sorted_characters:
        dict_char = char["char"]
        dict_num = char["num"]
        print(f"{dict_char}: {dict_num}")
    

    print("============= END ===============")
main()


