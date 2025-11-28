# smart_text_analyzer.py

"""
Eagle Point AI — Smart Text Analyzer
Author: KingFillari
Description:
    A Python project for analyzing text input for the Eagle Point AI Full-Stack Developer Technical Assessment.
    Provides:
        - Total word count
        - Average word length (2 decimals)
        - Longest word(s), including ties
        - Word frequency (case-insensitive)

Requirements:
    - Python 3.8+
    - No external libraries required
"""

# Import built-in string module to access string constants like punctuation
import string

# Import Counter to count occurrences of words easily
from collections import Counter

# Import typing for type hints
from typing import List, Dict

def normalize_text(text: str) -> str:
    """
    Converts the input text to lowercase and removes punctuation.

    Args:
        text (str): Input string to normalize.

    Returns:
        str: Normalized text without punctuation and in lowercase.
    """
    # Convert the entire text to lowercase for case-insensitive analysis
    text = text.lower()

    # Create a translation table to remove all punctuation characters
    translator = str.maketrans("", "", string.punctuation)

    # Apply the translation table to remove punctuation
    return text.translate(translator)


def smart_text_analyzer(text: str) -> Dict:
    """
    Analyzes the input text and returns word count, average word length,
    longest word(s), and word frequency.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with analysis results:
            - word_count (int): Total number of words
            - average_word_length (float): Average length of words, rounded to 2 decimals
            - longest_words (List[str]): All words with maximum length
            - word_frequency (Dict[str, int]): Frequency of each word (case-insensitive)
    """

    # Normalize the text: lowercase and remove punctuation
    normalized_text = normalize_text(text)

    # Edge case: If the text is empty or only spaces, return empty results
    if not normalized_text.strip():
        return {
            "word_count": 0,            # No words
            "average_word_length": 0.0, # Average length 0
            "longest_words": [],        # No longest words
            "word_frequency": {}        # Empty frequency dictionary
        }

    # Split the text into words based on spaces
    words = normalized_text.split()

    # Count total words
    word_count = len(words)

    # Calculate total length of all words
    total_length = sum(len(word) for word in words)

    # Compute average word length and round to 2 decimals
    average_word_length = round(total_length / word_count, 2)

    # Find the length of the longest word
    max_length = max(len(word) for word in words)

    # Collect all words that have the maximum length (handles ties)
    longest_words = [word for word in words if len(word) == max_length]

    # Count frequency of each word using Counter and convert to a dictionary
    word_frequency = dict(Counter(words))

    # Return all analysis results in a dictionary
    return {
        "word_count": word_count,
        "average_word_length": average_word_length,
        "longest_words": longest_words,
        "word_frequency": word_frequency
    }


# Optional: Allows the script to be run directly from the command line
if __name__ == "__main__":
    # Prompt the user to enter a text string
    input_text = input("Enter text to analyze: ")

    # Call the smart_text_analyzer function with the input
    result = smart_text_analyzer(input_text)

    # Print the results in a readable format
    print("\nAnalysis Result:")
    print(f"Total words: {result['word_count']}")
    print(f"Average word length: {result['average_word_length']}")
    print(f"Longest words: {result['longest_words']}")
    print("Word frequency:")

    # Print each word and its frequency
    for word, freq in result["word_frequency"].items():
        print(f"  {word}: {freq}")
