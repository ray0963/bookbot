BOOK_PATH = "books/frankenstein.txt"


def open_book(book_path: str) -> str:
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    words = text.split()
    character_counts = {}
    for word in words:
        for char in word:
            if char.lower() in character_counts:
                character_counts[char.lower()] += 1
            elif char.isalpha():
                character_counts[char.lower()] = 1
    return character_counts


def print_char_count(counts: dict) -> str:
    char_print = ""
    sorted_counts = {
        k[0]: k[1]
        for k in sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    }
    for key in sorted_counts:
        char_print += (
            f"The '{key}' character was found {str(sorted_counts[key])} times \n"
        )
    return char_print


def create_report(book_path: str) -> str:
    book_text = open_book(book_path)
    char_counts = count_characters(book_text)
    report = f"""
--- Begin report of {book_path} ---
{count_words(book_text)} words found in the document

{print_char_count(char_counts)}
--- End report ---
"""
    return report


def main():
    print(create_report(BOOK_PATH))


if __name__ == "__main__":
    main()
