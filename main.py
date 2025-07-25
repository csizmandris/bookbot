import sys
from stats import (
    get_book_text,
    count_words,
    count_characters,
    sort_list,
)

sys.argv

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_words(text)
        characters = count_characters(text)
        sorted_list = sort_list(characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for items in sorted_list:
            print(f"{items["character"]}: {items["num"]}")
        print("============= END ===============")

main()