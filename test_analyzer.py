test_texts = [
    # Test 1: Basic functionality
    "The quick brown fox jumps over the lazy dog",
    
    # Test 2: Empty string
    "",
    
    # Test 3: Punctuation handling
    "Hello, world! This... is a test? Of punctuation!",
    
    # Test 4: Mixed case for frequency testing
    "Python PYTHON python PythOn",
    
    # Test 5: Tied longest words
    "I saw a big red car and a small blue bike",
    
    # Test 6: Single word
    "Hello",
    
    # Test 7: Apostrophes in contractions
    "Don't can't won't it's",
    
    # Test 8: Numbers and mixed characters
    "Test123 with numbers 456 and symbols #$%",
    
    # Test 9: Multiple spaces
    "Hello   world    with    multiple   spaces",
    
    # Test 10: Special characters only
    "!!! ### $$$ %%%",
    
    # Test 11: Whitespace only
    "   \n\t  \n",
    
    # Test 12: Long text for performance
    " ".join(["word"] * 100)  # 100 repetitions of "word"
]