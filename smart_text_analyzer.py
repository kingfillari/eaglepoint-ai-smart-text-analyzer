"""
Eagle Point AI — Smart Text Analyzer
Full-Stack Developer Technical Assessment

A robust text analysis tool that provides comprehensive insights into text content.
Features: word count, average word length, longest words, and word frequency analysis.

Author: Filimon Gebre(kingfillari)
Date: November 28,2025
"""

# Import the regular expression module for text pattern matching and manipulation
import re
# Import string module for accessing string constants like punctuation characters
import string
# Import Counter class from collections module for efficient word frequency counting
from collections import Counter
# Import type hinting utilities for better code documentation and IDE support
from typing import Dict, List, Union


def smart_text_analyzer(text: str) -> Dict[str, Union[int, float, List[str], Dict[str, int]]]:
    """
    Analyzes input text and returns comprehensive text statistics.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        Dict containing:
            - word_count (int): Total number of words
            - average_word_length (float): Average word length rounded to 2 decimals
            - longest_words (List[str]): List of longest word(s), including ties
            - word_frequency (Dict[str, int]): Word frequency counts (case-insensitive)
            
    Raises:
        TypeError: If input is not a string
    """
    
    # Input validation - check if the provided input is actually a string
    if not isinstance(text, str):
        # If not a string, raise TypeError with informative message showing actual type
        raise TypeError(f"Expected string input, got {type(text).__name__}")
    
    # Handle empty string and whitespace-only input scenarios
    # Check if text is empty, None, or contains only whitespace characters
    if not text or text.isspace():
        # Return default empty results for invalid/empty input
        return {
            "word_count": 0,                    # Zero words counted
            "average_word_length": 0.0,         # Zero average length
            "longest_words": [],                # Empty list for longest words
            "word_frequency": {}                # Empty dictionary for word frequencies
        }
    
    # Normalize text: convert to lowercase and remove punctuation for consistent processing
    normalized_text = _normalize_text(text)
    
    # Extract words by splitting normalized text and filter out any empty strings
    # This handles cases with multiple consecutive spaces
    words = [word for word in normalized_text.split() if word]
    
    # Handle edge case where normalization removes all content (e.g., only punctuation)
    if not words:
        # Return empty results similar to empty input scenario
        return {
            "word_count": 0,
            "average_word_length": 0.0,
            "longest_words": [],
            "word_frequency": {}
        }
    
    # Calculate statistics by calling specialized helper functions
    word_count = len(words)                                # Count total valid words
    average_word_length = _calculate_average_word_length(words)  # Compute average word length
    longest_words = _find_longest_words(words)             # Find all longest words
    word_frequency = _calculate_word_frequency(words)      # Count frequency of each word
    
    # Return comprehensive analysis results as a structured dictionary
    return {
        "word_count": word_count,              # Total number of words found
        "average_word_length": average_word_length,  # Average character count per word
        "longest_words": longest_words,        # List of word(s) with maximum length
        "word_frequency": word_frequency       # Dictionary mapping words to their counts
    }


def _normalize_text(text: str) -> str:
    """
    Normalizes text by converting to lowercase and removing punctuation.
    
    Args:
        text (str): Input text to normalize
        
    Returns:
        str: Normalized text with lowercase and no punctuation
    """
    # Convert entire text to lowercase to ensure case-insensitive analysis
    text = text.lower()
    
    # Remove punctuation using regex while preserving apostrophes within words
    # string.punctuation.replace("'", '') removes apostrophe from punctuation list
    # re.escape() ensures special regex characters in punctuation are treated literally
    # This regex pattern matches any character in the punctuation set (except apostrophe)
    text = re.sub(rf"[{re.escape(string.punctuation.replace("'", ''))}]", '', text)
    
    # Return the cleaned and normalized text ready for analysis
    return text


def _calculate_average_word_length(words: List[str]) -> float:
    """
    Calculates the average word length from a list of words.
    
    Args:
        words (List[str]): List of words
        
    Returns:
        float: Average word length rounded to 2 decimal places
    """
    # Calculate total characters by summing the length of each word in the list
    total_chars = sum(len(word) for word in words)
    
    # Compute average by dividing total characters by number of words
    average = total_chars / len(words)
    
    # Round to 2 decimal places for clean, readable output
    return round(average, 2)


def _find_longest_words(words: List[str]) -> List[str]:
    """
    Finds the longest word(s) in the list, handling ties.
    
    Args:
        words (List[str]): List of words
        
    Returns:
        List[str]: List of longest word(s), sorted alphabetically
    """
    # Check for empty word list to avoid errors in max() function
    if not words:
        return []  # Return empty list if no words provided
    
    # Find the maximum word length by checking length of each word
    max_length = max(len(word) for word in words)
    
    # Collect all words that have length equal to the maximum length found
    longest_words = [word for word in words if len(word) == max_length]
    
    # Remove duplicates using set() and sort alphabetically for consistent output
    return sorted(list(set(longest_words)))


def _calculate_word_frequency(words: List[str]) -> Dict[str, int]:
    """
    Calculates word frequency using Counter.
    
    Args:
        words (List[str]): List of words
        
    Returns:
        Dict[str, int]: Dictionary with words as keys and frequencies as values
    """
    # Use Counter to efficiently count occurrences of each word in the list
    # Convert Counter object to regular dictionary for cleaner return type
    return dict(Counter(words))


def main():
    """
    Command-line interface for the Smart Text Analyzer.
    """
    # Print application header and branding
    print("=== Eagle Point AI — Smart Text Analyzer ===")
    # Display user instructions for input
    print("Enter your text (press Ctrl+D or Ctrl+Z to finish):")
    # Print separator line for better visual organization
    print("-" * 50)
    
    # Use try-except block to handle user interruptions and errors gracefully
    try:
        # Initialize empty list to store multiple lines of user input
        lines = []
        
        # Continuous loop to read user input line by line
        while True:
            try:
                # Read a single line of input from user
                line = input()
                # Add the line to our collection of lines
                lines.append(line)
            except EOFError:
                # Break loop when user signals end of input (Ctrl+D/Ctrl+Z)
                break
        
        # Combine all input lines into a single text string with newline separators
        text = "\n".join(lines)
        
        # Check if the combined text contains only whitespace or is empty
        if not text.strip():
            # Inform user and exit if no meaningful text was provided
            print("\nNo text provided. Exiting.")
            return  # Exit the function early
        
        # Analyze the provided text using our main analyzer function
        result = smart_text_analyzer(text)
        
        # Display results section with formatted headers
        print("\n" + "=" * 50)  # Print separator line
        print("ANALYSIS RESULTS")  # Results section title
        print("=" * 50)  # Print separator line
        
        # Display individual statistics with clear labels
        print(f"Total Word Count: {result['word_count']}")  # Show total words
        print(f"Average Word Length: {result['average_word_length']}")  # Show average length
        print(f"Longest Word(s): {', '.join(result['longest_words'])}")  # Show longest words as comma-separated list
        
        # Display word frequency section
        print("\nWord Frequency:")  # Frequency section header
        print("-" * 20)  # Sub-section separator
        
        # Iterate through words sorted alphabetically for consistent display
        for word, count in sorted(result['word_frequency'].items()):
            # Print each word with its frequency count
            print(f"{word}: {count}")
            
    except KeyboardInterrupt:
        # Handle user pressing Ctrl+C gracefully
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        # Catch any unexpected errors and display friendly error message
        print(f"\nAn error occurred: {e}")


# Standard Python idiom to check if this script is being run directly
if __name__ == "__main__":
    # If script is run directly (not imported), execute the main function
    main()