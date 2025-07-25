def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    characters = count_characters(text)
    sorted_list = sort_list(characters)
    #printable_list = function? str.isalpha()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in sorted_list:
        print(f"{items["character"]}: {items["num"]}")
    print("============= END ===============")


from stats import get_book_text

from stats import count_words

from stats import count_characters

from stats import sort_list

main()