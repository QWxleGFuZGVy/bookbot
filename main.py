#!/usr/bin/env python3

import sys

from stats import get_num_words, get_book_text, get_char_count, sort_dict


def main(book):
    #book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    content = get_book_text(book)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    d = get_char_count(content)
    print("--------- Character Count -------")
    l1 = sort_dict(d)
    l1.reverse()

    for x in l1:
        k = x["char"]
        v = x["num"]
        print(f"{k}: {v}")


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    main(sys.argv[1])
