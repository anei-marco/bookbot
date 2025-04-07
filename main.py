import sys
from stats import get_num_words, count_characters, sort_characters


def get_book_text(filepath):
    """Get the full text from a file"""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found")
        sys.exit(1)

    num_words = get_num_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
