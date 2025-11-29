# Eagle Point AI - Smart Text Analyzer

A comprehensive Python text analysis tool built for the Eagle Point AI Full-Stack Developer Technical Assessment. This application provides detailed insights into text content with robust edge-case handling and professional code quality.

## ✨ Features

- **Word Count**: Accurate total word counting, ignoring multiple spaces and empty strings
- **Average Word Length**: Mean word length calculation with precise floating-point results
- **Longest Words Identification**: Handles ties and provides all words with maximum length
- **Word Frequency Analysis**: Case-insensitive word occurrence counting with punctuation handling
- **Robust Text Processing**: Comprehensive edge-case handling including empty input validation

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/kingfillari/eaglepoint-ai-smart-text-analyzer.git
cd eaglepoint-ai-smart-text-analyzer

# No external dependencies required - uses only Python standard library
# Verify Python installation
python --version
```

## 📖 Usage

### Basic Usage
```python
from text_analyzer import analyze_text

# Analyze your text
sample_text = "Hello world hello universe world"
result = analyze_text(sample_text)
print(result)
```

### Expected Output
```python
{
    'word_count': 5,
    'average_word_length': 5.4,
    'longest_words': ['universe'],
    'word_frequency': Counter({'hello': 2, 'world': 2, 'universe': 1})
}
```

### Individual Functions
You can also use the analysis functions independently:

```python
from text_analyzer import word_count, average_word_length, longest_words, word_frequency

text = "Your sample text here"
print(f"Word count: {word_count(text)}")
print(f"Average word length: {average_word_length(text)}")
print(f"Longest words: {longest_words(text)}")
print(f"Word frequency: {word_frequency(text)}")
```

## 🧪 Testing

The module includes comprehensive error handling and edge case management:

```python
# Test with various inputs
test_cases = [
    "Hello world!",  # Normal text with punctuation
    "Multiple   spaces   between   words",  # Multiple spaces
    "UPPERCASE lowercase MixedCase",  # Case variations
    "word",  # Single word
]

for test in test_cases:
    try:
        result = analyze_text(test)
        print(f"Input: '{test}'")
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Input: '{test}'")
        print(f"Error: {e}\n")
```

## Edge Cases Handled

- ✅ Empty strings and whitespace-only input
- ✅ Multiple consecutive spaces
- ✅ Punctuation in words
- ✅ Mixed case sensitivity
- ✅ Single word inputs
- ✅ Multiple words with same maximum length

## 🔧 API Reference

analyze_text(text)  
Main function that returns a comprehensive analysis dictionary.

Parameters:
- text (str): Input text to analyze

Returns:
- dict with keys:
  - word_count (int): Total number of words
  - average_word_length (float): Average length of words
  - longest_words (list): All words with maximum length
  - word_frequency (Counter): Frequency count of each word

Raises:
- ValueError: If input text is empty or contains only whitespace

word_count(text)  
Counts total words in text, ignoring empty strings.

average_word_length(text)  
Calculates average length of all words.

longest_words(text)  
Finds all words with the maximum length.

word_frequency(text)  
Returns frequency count of each word (case-insensitive, punctuation removed).

## 💡 Technical Details

### Implementation Highlights
- Pure Functions: Each function has single responsibility and no side effects
- Performance Optimized: Uses list comprehensions and built-in functions for efficiency
- Memory Efficient: Generators and early filtering reduce memory footprint
- Standard Library Only: No external dependencies required

### Algorithm Complexity
- Time Complexity: O(n) for all operations, where n is text length
- Space Complexity: O(n) for word storage and frequency counting

### Design Decisions
- Python Choice: Selected for excellent text processing capabilities and readability
- Functional Approach: Pure functions for better testability and maintainability
- Robust Input Handling: Comprehensive validation and edge case management
- Performance Focus: Leveraged Python's optimized built-in functions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions.

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/kingfillari/eaglepoint-ai-smart-text-analyzer.git
cd eaglepoint-ai-smart-text-analyzer

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Running Tests
Add your test cases to the examples provided in the main module and run with:

```bash
python text_analyzer.py
```

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Fillimon (KingFillari)

GitHub: @kingfillari(https://github.com/kingfillari/eaglepoint-ai-smart-text-analyzer)

LinkedIn: https://www.linkedin.com/in/fillimon-gebre

## 🔗 Related Projects

- Async Data Fetcher with Retry
- Rate Limiter

B
```// filepath: e:\SPECIAL\eaglepoint-ai-smart-text-analyzer\README.md
# Eagle Point AI - Smart Text Analyzer

A comprehensive Python text analysis tool built for the Eagle Point AI Full-Stack Developer Technical Assessment. This application provides detailed insights into text content with robust edge-case handling and professional code quality.

## ✨ Features

- **Word Count**: Accurate total word counting, ignoring multiple spaces and empty strings
- **Average Word Length**: Mean word length calculation with precise floating-point results
- **Longest Words Identification**: Handles ties and provides all words with maximum length
- **Word Frequency Analysis**: Case-insensitive word occurrence counting with punctuation handling
- **Robust Text Processing**: Comprehensive edge-case handling including empty input validation

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/kingfillari/eaglepoint-ai-smart-text-analyzer.git
cd eaglepoint-ai-smart-text-analyzer

# No external dependencies required - uses only Python standard library
# Verify Python installation
python --version
```

## 📖 Usage

### Basic Usage
```python
from text_analyzer import analyze_text

# Analyze your text
sample_text = "Hello world hello universe world"
result = analyze_text(sample_text)
print(result)
```

### Expected Output
```python
{
    'word_count': 5,
    'average_word_length': 5.4,
    'longest_words': ['universe'],
    'word_frequency': Counter({'hello': 2, 'world': 2, 'universe': 1})
}
```

### Individual Functions
You can also use the analysis functions independently:

```python
from text_analyzer import word_count, average_word_length, longest_words, word_frequency

text = "Your sample text here"
print(f"Word count: {word_count(text)}")
print(f"Average word length: {average_word_length(text)}")
print(f"Longest words: {longest_words(text)}")
print(f"Word frequency: {word_frequency(text)}")
```

## 🧪 Testing

The module includes comprehensive error handling and edge case management:

```python
# Test with various inputs
test_cases = [
    "Hello world!",  # Normal text with punctuation
    "Multiple   spaces   between   words",  # Multiple spaces
    "UPPERCASE lowercase MixedCase",  # Case variations
    "word",  # Single word
]

for test in test_cases:
    try:
        result = analyze_text(test)
        print(f"Input: '{test}'")
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Input: '{test}'")
        print(f"Error: {e}\n")
```

## Edge Cases Handled

- ✅ Empty strings and whitespace-only input
- ✅ Multiple consecutive spaces
- ✅ Punctuation in words
- ✅ Mixed case sensitivity
- ✅ Single word inputs
- ✅ Multiple words with same maximum length

## 🔧 API Reference

analyze_text(text)  
Main function that returns a comprehensive analysis dictionary.

Parameters:
- text (str): Input text to analyze

Returns:
- dict with keys:
  - word_count (int): Total number of words
  - average_word_length (float): Average length of words
  - longest_words (list): All words with maximum length
  - word_frequency (Counter): Frequency count of each word

Raises:
- ValueError: If input text is empty or contains only whitespace

word_count(text)  
Counts total words in text, ignoring empty strings.

average_word_length(text)  
Calculates average length of all words.

longest_words(text)  
Finds all words with the maximum length.

word_frequency(text)  
Returns frequency count of each word (case-insensitive, punctuation removed).

## 💡 Technical Details

### Implementation Highlights
- Pure Functions: Each function has single responsibility and no side effects
- Performance Optimized: Uses list comprehensions and built-in functions for efficiency
- Memory Efficient: Generators and early filtering reduce memory footprint
- Standard Library Only: No external dependencies required

### Algorithm Complexity
- Time Complexity: O(n) for all operations, where n is text length
- Space Complexity: O(n) for word storage and frequency counting

### Design Decisions
- Python Choice: Selected for excellent text processing capabilities and readability
- Functional Approach: Pure functions for better testability and maintainability
- Robust Input Handling: Comprehensive validation and edge case management
- Performance Focus: Leveraged Python's optimized built-in functions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions.

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/kingfillari/eaglepoint-ai-smart-text-analyzer.git
cd eaglepoint-ai-smart-text-analyzer

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Running Tests
Add your test cases to the examples provided in the main module and run with:

```bash
python eaglepoint-ai-smart-text-analyzer.py
```

