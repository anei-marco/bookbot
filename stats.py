from collections import defaultdict


def get_num_words(text):
    """Count the number of words in the given text"""
    words = text.split()
    return len(words)


def count_characters(text):
    """Count the frequency of each character in the text (case-insensitive)"""
    char_count = defaultdict(int)
    for char in text.lower():
        char_count[char] += 1
    return char_count


def sort_characters(char_counts):
    """
    Convert character counts to a sorted list of dictionaries,
    filtering out non-alphabetical characters and sorting by count (descending)
    """
    filtered_chars = [
        {"char": char, "count": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    filtered_chars.sort(key=lambda item: item["count"], reverse=True)
    return filtered_chars
