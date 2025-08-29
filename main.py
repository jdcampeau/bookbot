import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: None

from stats import word_char_analysis

word_char_analysis(sys.argv[1])




